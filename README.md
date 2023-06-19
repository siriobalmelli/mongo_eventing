# MongoDB Eventing Example in Python

You will need [Nix](https://nixos.org/);
to install it use [this installer](https://zero-to-nix.com/concepts/nix-installer):

    curl --proto '=https' --tlsv1.2 -sSf -L https://install.determinate.systems/nix | sh -s -- install

Enter a development shell:

    nix develop

Subscribe to events:

    ./consumer.py

Publish a new event:

    ./producer.py
