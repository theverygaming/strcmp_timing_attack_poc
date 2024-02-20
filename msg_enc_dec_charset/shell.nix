with import <nixpkgs> { };
stdenv.mkDerivation {
  name = "msg_enc_dec_charset";
  buildInputs = [
    python311
  ];
}
