{
  description = "Music Note Learning Generator - Generate random music note exercises for piano beginners";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};

        # Package that wraps the note generator script
        note-generator-pkg = pkgs.stdenv.mkDerivation {
          pname = "note-generator";
          version = "1.0.0";
          src = ./.;

          buildInputs = [ pkgs.python3 ];

          installPhase = ''
            mkdir -p $out/bin
            mkdir -p $out/share/note-generator

            # Copy the Python script
            cp ${./note_generator.py} $out/share/note-generator/note_generator.py

            # Create wrapper script
            cat > $out/bin/note-generator <<EOF
            #!${pkgs.bash}/bin/bash
            exec ${pkgs.python3}/bin/python3 $out/share/note-generator/note_generator.py "\$@"
            EOF

            chmod +x $out/bin/note-generator
          '';

          meta = with pkgs.lib; {
            description = "Generate random music note exercises for piano beginners";
            license = licenses.gpl3Only;
            platforms = platforms.unix;
          };
        };

      in
      {
        # Default package
        packages.default = note-generator-pkg;

        # Applications
        apps = {
          # Default app: run the note generator
          default = {
            type = "app";
            program = "${note-generator-pkg}/bin/note-generator";
          };

          # Test runner app
          tests = {
            type = "app";
            program = toString (pkgs.writeShellScript "run-tests" ''
              cd ${./.}
              exec ${pkgs.python3}/bin/python3 -m unittest discover -s tests -p "test_*.py" -v
            '');
          };
        };

        # Development shell
        devShells.default = pkgs.mkShell {
          buildInputs = with pkgs; [
            python3
            python3Packages.black
            git
          ];

          shellHook = ''
            echo "🎵 Music Note Generator Development Environment"
            echo "  Python: $(python3 --version)"
            echo "  Black: $(black --version | head -n1)"
            echo ""
            echo "Commands:"
            echo "  python note_generator.py    - Run the generator"
            echo "  python -m unittest discover - Run tests"
            echo "  black note_generator.py     - Format code"
            echo ""

            # Set custom prompt to indicate nix environment
            export PS1="\[\033[1;34m\][nix-flake]\[\033[0m\] \w $ "
          '';
        };

        # Formatter for Nix files
        formatter = pkgs.nixpkgs-fmt;
      }
    );
}
