# Clean-room replication report

## Identity and scope

- Replicator:
- Affiliation or public profile:
- Date:
- RGΦ commit reviewed:
- Independent implementation repository/archive:
- Language and version:
- Operating system:
- Hardware:

## Independence declaration

- [ ] The implementation was designed independently.
- [ ] No code was copied from `src/rgphi` or `scripts/compact_bfs.cpp`.
- [ ] Exact arithmetic was used for theorem-critical decisions.
- [ ] All discrepancies are reported below.

## Exact result table

| target | expected | reproduced | status |
|---|---:|---:|---|
| terminal states | 23 |  |  |
| attempted terminal T/S checks | 46 |  |  |
| admissible terminal escapes | 0 |  |  |
| tau_1 | 45 |  |  |
| tau_2 | 85 |  |  |
| tau_3 | 120 |  |  |
| tau_4 | 162 |  |  |
| continuation from 128/129 | 87 |  |  |
| continuation from 1202/1203 | 139 |  |  |
| continuation from 11156/11157 | 168 |  |  |
| chronology interval | [10.6197, 11.643) |  |  |
| nonnesting interval | [10.6197, 11.01) |  |  |
| C8 size | 8 |  |  |
| C8 maximum portal height | 13 |  |  |
| D<=500 states | 76094 |  |  |
| D<=500 edges | 109254 |  |  |
| D<=500 SCCs | 23176 |  |  |
| closed SCCs | 153 |  |  |
| finite closures | 1502 |  |  |

## Commands and runtime

## Hashes and machine-readable output

## Discrepancies

For every mismatch, report the first divergent state/layer and do not silently alter definitions to obtain agreement.

## Conclusion

- [ ] complete reproduction
- [ ] partial reproduction
- [ ] failed reproduction
- [ ] ambiguous specification requiring author clarification
