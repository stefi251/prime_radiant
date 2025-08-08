import marimo as mo
import plotly.express as px

# 1) Instantiate the app
app = mo.App(app_title="Prime Radiant Interactive Demo")

# 2) Reactive slider cell
@app.cell
def make_slider(mo):
    # Creates a slider UI from 1 to 10 labeled "x"
    slider = mo.ui.slider(start=1, stop=10, step=1, label="x")
    return (slider,)

# 3) Dependent computation
@app.cell
def compute_double(x):
    # x is the slider object; x.value is its current number
    return (x.value * 2,)

# 4) Display the result in markdown
@app.cell
def show_double(mo, compute_double):
    mo.md(f"**2 × x = {compute_double}**")
    return

# 5) Interactive scatter plot with click-to-select
@app.cell
def scatter_with_selector(mo):
    df = px.data.iris()
    fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")
    # click_data watches for clicks and returns the point you clicked on
    selector = mo.ui.click_data(fig)
    return (fig, selector)

@app.cell
def show_selection(mo, selector):
    mo.md(f"You clicked on: {selector}")
    return

# 6) AI-powered Q&A
@app.cell
def ask_marimo(mo):
    # A simple text box for your question
    prompt = mo.ui.text_input(label="Ask Marimo anything")
    return (prompt,)

@app.cell
def marimo_answer(mo, ask_marimo):
    if ask_marimo:  # only fire once you type something
        answer = mo.ai.ask(ask_marimo)
        mo.md(answer)
    return

if __name__ == "__main__":
    app.run()  # launches the Marimo web app