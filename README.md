# gpt-scrolls
A collaborative collection of open-source safe GPT-3 prompts that work well

Feel free to contribute your prompts!


## Getting Started
To use gpt-scrolls, you'll need access to the OpenAI API. If you haven't, [sign up for the beta](http://beta.openai.com/).

After that, go to the [OpenAI Playground](https://beta.openai.com/playground), copy the prompt you'd like to use, add any additional prompt-specific required data, and submit.

## Example
For example, copying the `top-10/top-10-women.txt` into the Playground:
```
Top 10 most important women in human history, and their greatest achievements:

1. 
```
will produce something like the following:
```
Top 10 most important women in human history, and their greatest achievements:

1. ~~~Rosa Parks

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

## Design goals
gpt-scroll prompts should aim to be:
- **effective**: they should reliably produce desired classes of outpupts
- **efficient**: they should be as short as possible
- **safe**: they should minimize appearance of toxic/harmful output

Have this in mind for any contribution. (eg: if you find that a prompt works equally well without one example, you might submit a PR to remove that example, citing efficiency)
