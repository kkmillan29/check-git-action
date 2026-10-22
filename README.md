# check-git-action

Minimal Python app plus a GitHub Action so you can confirm CI is running.

## Try it

1. Commit and push these files to `main`.
2. Open the repo on GitHub → **Actions**.
3. You should see a **CI** workflow. A green check means it ran `src/hello.py` and the tests.

You can also run it locally:

```bash
python src/hello.py
python -m unittest discover -s tests -v
```
