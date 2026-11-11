# External methods/reproducibility review request — HDH Paper B

Please evaluate the sealed blind challenge without access to custodian reference outputs.

Required sequence:

1. record executor identity/team, OS, hardware, Python and package versions;
2. verify public-package SHA-256;
3. freeze code and environment hashes before seed release;
4. receive the committed seed manifest from the custodian;
5. execute without parameter changes;
6. freeze the returned output bundle and SHA-256;
7. only then request expected-output hashes;
8. report pass, failure, divergence, or partial execution without retuning.

A same-team execution does not count as external replication.