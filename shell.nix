{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = [
    (pkgs.python311.withPackages (ps: [
      ps.reportlab
    ]))
  ];

  shellHook = ''
    echo -e "\e[31mRunning NixShell"
    FILENAME=$(find txts/ -type f -mtime 0)
    echo $FILENAME

    python main.py $FILENAME
    exit
  '';
}

