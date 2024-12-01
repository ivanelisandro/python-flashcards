# Stage 2:

For stage 2 the user also tries to guess the answer.
This is a preview for the actual implementation in future stages. 
Three inputs:

- first represents the "term" (flashcard front)
- second represents the "definition" (flashcard back)
- third represents an attempt to answer the flashcard that was just created

Possible outputs:

- `Your answer is wrong...` if the answer doesn't match the definition;
- `Your answer is right!` if the answer matches the definition.


## Examples:

Example 1: the user's answer is correct

Input (a term, a definition, an answer):

```
> print()
> outputs text
> outputs text
```

Output:

```
Your answer is right!
```

Example 2: the user's answer is incorrect

Input (a term, a definition, an answer):

```
> Jetbrains
> A place for people who love to code
> A place for people who hate to code
```

Output:

```
Your answer is wrong...
```
