# Project survey

Notes on which public repos belong on the portfolio, and where each one sits.
Surveyed 2026-10-26 from each repo's README, layout and main files.

## On the site

| Group | Repo | What it is | Links |
|---|---|---|---|
| Web apps | hood | Zoomable jigsaw map for learning LA County neighborhoods: pieces connect only as true geographic neighbors; zoom regions → groups → neighborhoods. | `/hood/` |
| Web apps | consciousness-map | Phone-first guide to theories of consciousness on the Landscape of Consciousness taxonomy: main quiz, per-category quizzes, adaptive mega quiz, share links, Russian. | `/consciousness-map/` |
| Web apps | factorio-hub | Resource-planning site for Factorio (Nuxt, PrimeVue). | factoriohub.net |
| Web apps | eggo | Mobile-first egg tracker for a backyard flock; Google Sheet backend via Apps Script, offline queue. | `/eggo/` |
| Web apps | resonate | Vocal pitch + waveform (YIN pitch detection, Web Audio). | `/resonate/` |
| Web apps | strooplang | Stroop-effect test in multiple languages (Vue 3, Vitest, Cypress). | `/strooplang/` |
| Libraries & tools | ti-js | TI-Basic interpreter/runtime for the browser, on npm. Links ti84-entertainment as "the old programs". | `/ti-js/` |
| Libraries & tools | urth | Converts the *Lexicon Urthus* into a Kindle dictionary. | source only |
| Just for fun | vanity | Vanity license-plate generator with CA DMV availability check. Lives in maximilian-reinsel/vanity (most commits are David's). | source only |
| Just for fun | wordle | Wordle solver bot. | source only |
| Just for fun | madness (+ madness-results) | March Madness bracket predictor. | source only |
| Just for fun | riddles | Jekyll site of puzzle write-ups. | `/riddles/` |
| Userscripts | letteropener | Love Letter card counting on Board Game Arena. | source only |
| Userscripts | command.games | Dominion randomizer for dominion.games. | source only |
| Userscripts | wikiwidth | "Toggle width" button for MediaWiki pages. | source only |
| Open source | KingdomCreator (fork) | Maintained fork of Dominion Randomizer, served at kingdomfork.com. | kingdomfork.com |
| Open source | ripgrep (fork) | Contributed `--ignore-file-case-insensitive` (ripgrep 11.0.0, commit 718a00f). | upstream commit |

Folded into other cards rather than listed: consciousness-theory-quiz (the
earlier version of consciousness-map, linked as "earlier quiz") and
ti84-entertainment (linked from ti-js).

## Left off

| Repo | Why |
|---|---|
| BitwardenBackup | Personal backup utility. |
| telegram-drillbot | 2019 Telegram menu-bot library; dated. |
| wikimit (+ wikimit-hub) | Prototype; README says "Not ready yet". |
| btw | Personal Arch Linux install script. |
| bitwarden-clients, azure-devops-cli-extension, pegjs, keep-a-changelog, vanity (davidtorosyan/vanity) | Forks with no commits by David, or empty. |

## To check

- Demo URLs were not verified from the survey sandbox: `/resonate/`,
  `/strooplang/`, `/riddles/` and `/consciousness-theory-quiz/` in particular.
- ti-js and riddles READMEs link to davidtorosyan.com; the site is now
  www.jimbo84.com.
- resonate has no README; strooplang's README is Vite boilerplate.
- Only hood and ti-js have icons in `assets/icons/`; the other cards show none.
