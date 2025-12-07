import wikipedia
import warnings

warnings.filterwarnings("ignore", category = UserWarning, module = 'wikipedia')
lang = input("fr for French\nes for Spanish\nde for German\nit for Italian\nen for English\nEnter language you want answer in: ")

wikipedia.set_lang(lang)

while True:
    question = input("Q: ")

    try:
        print(wikipedia.summary(question, sentences = 2, auto_suggest=False))
    except wikipedia.exceptions.DisambiguationError as e:
        print("⚠️ This term has multiple meanings. Be more specific.")
        print("Here are some options:")
        for option in e.options[:10]:  # show first 10 options
            print(" -", option)
    except wikipedia.exceptions.PageError:
        print("❌ Page not found, try another word.")