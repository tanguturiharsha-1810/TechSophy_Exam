import google.generativeai as genai

def gemini_insights(df, api_key):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.5-flash')
    # Use a sample of the DataFrame for prompt brevity
    sample = df.head(20).to_csv(index=False)
    prompt = (
        "Analyze the following personal finance transactions and provide insights, "
        "anomaly detection, and actionable recommendations:\n\n"
        f"{sample}\n\n"
        "Give your answer in bullet points."
        "give simple answers"
    )
    response = model.generate_content(prompt)
    return response.text
