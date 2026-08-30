# Cross-provider public readback — U429

Status: **PASS**  
Date: 2026-08-30

The independent verifier downloaded the complete public U429 payload from
both GitHub and Zenodo without credentials. Each provider exposes exactly nine
assets / 12,943,707 bytes. Filename, byte count, and SHA-256 match for every
asset, including the 2,427,379-byte complete R006 Volume II reader and the
6,106,435-byte deterministic source/backend archive.

The verifier also downloaded all eight release-checkpoint repository files at
immutable commit `0ea0e44992addc811552d6fd37689e59385272d5` and matched them
to the frozen local overlay. Zenodo record `22172396` is published and open;
the stable concept's latest endpoint resolves to that record. GitHub release
`379250341` is public, non-draft, and non-prerelease.

Cross-provider byte identity: **true**. Historical U397 publication remains
public and unchanged.
