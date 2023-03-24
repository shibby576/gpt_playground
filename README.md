# Data summarization with OpenAI

Live app: https://data-summarizer.herokuapp.com/

### What is this?
With all of the progress happening then in generative AI space, I felt compelled to learn more about some the current capabilities by building something simple. After a quick brainstorm and playing around in the OpenAI playground, it seemed like a really compelling capability of GPT3.5 is that it can summarize data/text rather well. 

This made me think back to all of the time that ive spent in the past generating beautiful tables or charts only having to spend just as long writing a nice written summary of what that chart is showing. With that painpoint in mind, I designed a prompt and wired it up with text-davinci-003 model to output nice summaries of data. 

The app is very simple (and not very good looking!) for now, but it was a great way to begin understanding how these models might be used. For example, this app simply provides a stock prompt to the model along with the user's input, which produces okay results. What can make it better is providing context or examples to further tailor the response. 

Further, what im more excited to try next is the idea of embeddings and fine tuning, which from what i understand are ways to tailor the existing models to custom data. To me, this is where the real power of these models reside, giving those witch unique data the ability to super charge these models into something noone else can. 

More enhancements to come here!
