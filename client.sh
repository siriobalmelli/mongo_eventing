#!/usr/bin/env bash
pushd "$(dirname "$0")" || exit 1

URL="mongodb+srv://cluster0.jf8lhh3.mongodb.net"
DB="Cluster0"
CERT="./X509-cert-6977471360154941700.pem"

mongosh \
	"$URL/$DB?authSource=%24external&authMechanism=MONGODB-X509" \
	--tls \
	--tlsCertificateKeyFile "$CERT" \
	--apiVersion 1 \
	--apiDeprecationErrors \
	--norc \
	"$@"
