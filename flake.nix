{
  description = "Python env for Advent of Code";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs {
          inherit system;
        };
      in
      {
        devShells.default = pkgs.mkShell {
          buildInputs = with pkgs; [
            python3
            python3Packages.z3-solver
            python3Packages.pip
            python3Packages.numpy
            python3Packages.networkx
          ];

          shellHook = ''
            echo "Python: $(python --version)"
            echo "Z3: $(python -c 'import z3; print(z3.get_version_string())' 2>/dev/null || echo 'available')"
          '';
        };
      }
    );
}
