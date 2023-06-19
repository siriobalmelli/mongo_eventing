{
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
    let
      pkgs = import nixpkgs { inherit system; };
    in
      rec {
        devShells.default = pkgs.mkShell {
          buildInputs = (with pkgs; [
            mongosh
            mongodb-tools
          ]) ++ (with pkgs; with python3Packages; [
            less
            dnspython
            pymongo
          ]);
        };
      }
    );
}
