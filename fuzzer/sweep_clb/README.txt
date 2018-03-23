Sweeps a bunch of different CLB configurations

Summary
Given CLB_NM
N => frame number
    Usually subtract 0x12, but sometimes 0x14
    max: 0x9f (160 - 1)
    A: 8b-9c
    B: 79-8a
    C: 67-78
    +
    D: 53-64
    E: 41-52
    F: 2f-40
    +
    G: 1b-2c
    H: 09-1a
M => frame bit offset
    Usually subtract 8, but sometimes 9
    max: 0x46 (71 - 1)
    A: 3e-3f
    B: 36-37
    C: 2e-2f
    +
    D: 25-26
    E: 1d-1e
    F: 15-16
    +
    G: 0c-0d
    H: 04-05

Coverage summary
All the frame numbers can be reasonably allocated to given CLBs + some scattered padding (maybe for clock routing)
Frame bit offsets have some large gaps
For now, locate a frame relative to base address 09_04
09 should be stable but 04 could possibly shift down a little

