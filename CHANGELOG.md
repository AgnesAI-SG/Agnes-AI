# Changelog

All notable public documentation, model catalog, quota, and integration updates for this repository are tracked here.

This changelog is a public reference. Model availability, RPM limits, subscription quotas, and pricing may change over time. Always confirm production-critical values in the official Agnes AI platform console.

## 2026-06-28

### Added

- Added `docs/TOKEN_PLAN_FAQ.md` with access types, Token Plan subscription quotas, RPM tables, and API key limit-pool behavior.

### Changed

- Updated public documentation version markers to `2026.06.28`.
- Updated video model RPM reference values:
  - Free / default: public request RPM `2`, actual executable RPM `1`.
  - Enterprise: public request RPM `2`, actual executable RPM `2`.
  - Token Plan: public request RPM `6`, actual executable RPM `5`.
- Clarified that Token Plan video subscription quota remains `500 seconds per day`.

## 2026-06-22

### Added

- Added public documentation status and version markers to `README.md`.
- Added current access and subscription quota summaries to `README.md`.
- Added detailed RPM tables to `MODEL_CATALOG.md`.
- Added current subscription quota reference values for Starter, Plus, and Pro plans.
- Added troubleshooting reference for common API status codes.
- Added support guidance for issues and discussions.
- Added minimal curl, Python, and Node.js examples.
- Added structured issue templates for API integration, bug reports, feature requests, and documentation issues.

### Changed

- Updated video polling guidance to prefer `video_id` for current video result queries.
- Clarified that current limits are operational reference values and may change.
- Clarified that `agnes-2.0-flash` currently uses a `256K` context window and `64K` max output reference limit after the June 2026 rollback from the temporary `1M` context window.
