{
  inputs = {
    nixpkgs.url = "nixpkgs/nixos-unstable";
    dev.url = "github:fmahnke/mkpkgs-dev";
  };

  outputs = { self, nixpkgs, ... }@inputs:
    with inputs;
    let
      system = "x86_64-linux";
      pkgs = nixpkgs.legacyPackages.${system};
      pythonPkgs = pkgs.python3.pkgs;
    in {
      packages.x86_64-linux.default = pythonPkgs.buildPythonPackage {
        pname = "pymk";
        version = "0.1.0";
        pyproject = true;

        src = ./python;

        buildInputs = with pythonPkgs; [ tomlkit setuptools ];

        nativeCheckInputs =
          [ inputs.dev.devShells.${system}.python.nativeBuildInputs ];

        checkPhase = ''
          nox
        '';
      };

      hydraJobs = { inherit (self) packages; };

      devShells.${system}.default = pkgs.mkShell {
        inputsFrom = [ inputs.dev.devShells.${system}.python ];

        inherit buildInputs;
      };
    };
}

