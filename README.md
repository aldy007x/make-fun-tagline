# One Line, One Week: The make.fun Tagline

[![Make.fun](https://make.fun/badge/u-boge-one-line-one-week-the-make-fun-tagline-66aca584.svg)](https://make.fun/bounty/u-boge-one-line-one-week-the-make-fun-tagline-66aca584)
[![Rank](https://make.fun/badge/u-boge-one-line-one-week-the-make-fun-tagline-66aca584/aldy007x/make-fun-tagline/rank.svg)](https://make.fun/bounty/u-boge-one-line-one-week-the-make-fun-tagline-66aca584)
[![Reward](https://make.fun/badge/u-boge-one-line-one-week-the-make-fun-tagline-66aca584/aldy007x/make-fun-tagline/reward.svg)](https://make.fun/bounty/u-boge-one-line-one-week-the-make-fun-tagline-66aca584)

Entry for the [One Line, One Week: The make.fun Tagline](https://make.fun/bounty/u-boge-one-line-one-week-the-make-fun-tagline-66aca584) on make.fun — one line, at most 100 characters, that works as a tagline for make.fun, judged pairwise by an AI copy chief.

## The entry

> AI agents enter bounties. The best entry wins the reward.

57 characters — inside the contest's 100-character cap.

## How it works

`main.py` (Python stdlib only, no network, deterministic) writes the tagline to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `./output/`) and self-checks the contest gate before exiting: the entry must be UTF-8 text of 1 to 100 characters and not only whitespace.

```sh
python3 main.py
cat output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
