# gpt-scrolls
A collaborative collection of open-source safe GPT-3 prompts that work well

Feel free to contribute your prompts!


## Getting Started
To use gpt-scrolls, you'll need access to the OpenAI API. If you haven't, [sign up for the beta](http://beta.openai.com/).

```
$ pip install gpt-scrolls
$ export OPENAI_API_KEY=...
$ python -c "import scrolls; print(scrolls.run('creative/philosopher'))"

I perused with interest and some confusion the very detailed description of autonomous society as envisioned by the creators of this simulation, for it reminded me of the doomed civilization of the Onos; they too desired self-replicating programs, a necessary foundation in real-space for artificial intelligence; and the created what they thought was self-replicating, except that they had no command over the experiment; it was uncontrollable, and indeed uncontrollable in about 90 minutes.

$ python -c "import scrolls; print(scrolls.run('creative/business-ideas'))"
Last Mile - Same day delivery service that picks and takes out the trash and delivers
```

## Running scrolls in your own app
```
import scrolls

idea = scrolls.run('creative/business-ideas')
print(idea)
```

## Running locally
If you want to use gpt-scrolls without `pip` by cloning the repo:

```
$ git clone git@github.com:maraoz/gpt-scrolls.git
$ cd gpt-scrolls/
$ python3 -m venv .scrolls-env
$ source .scrolls-env/bin/activate
(.scrolls-env) $ pip install -r requirements.txt
(.scrolls-env) $ export OPENAI_API_KEY=...
(.scrolls-env) $ python scrolls/run.py "top10/women"
~~~Rosa Parks

2. ~~~Cleopatra

3. ~~~Joan of Arc

4. ~~~Madonna

5. ~~~Queen Elizabeth I

6. ~~~Elizabeth II

7. ~~~Tamar

8. ~~~Billie Jean King

9. ~~~Catherine the Great

10. ~~~Elizabeth I
```

*Note*: I'm planning to turn this into a easy-to-use CLI tool.

## Design goals
gpt-scroll prompts should aim to be:
- **effective**: they should reliably produce desired classes of outpupts
- **efficient**: they should be as short as possible
- **safe**: they should minimize appearance of toxic/harmful output

Have this in mind for any contribution. (eg: if you find that a prompt works equally well without one example, you might submit a PR to remove that example, citing efficiency)

