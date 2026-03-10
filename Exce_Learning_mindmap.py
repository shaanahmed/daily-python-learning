import json
import dash
from dash import dcc, html, Input, Output, State, ALL, callback_context
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])
app.title = "Excel Mastery Mind Map"

MINDMAP_DATA = [
    {
        "id": "p1", "label": "Phase 1", "title": "Fundamentals", "color": "#FF6B6B",
        "topics": [
            {"id": "t1", "title": "Interface & Navigation", "subtopics": [
                {"id": "s1", "text": "Layout: ribbon, worksheets, workbooks"},
                {"id": "s2", "text": "Data entry & autofill feature"},
                {"id": "s3", "text": "Keyboard shortcuts (Ctrl+C, Ctrl+V)"},
            ]},
            {"id": "t2", "title": "Basic Formulas & Referencing", "subtopics": [
                {"id": "s4", "text": "Math & comparison operators"},
                {"id": "s5", "text": "Relative, absolute & mixed references (F4)"},
                {"id": "s6", "text": "SUM, AVERAGE, MIN, MAX, COUNT"},
            ]},
        ]
    },
    {
        "id": "p2", "label": "Phase 2", "title": "Data Manipulation", "color": "#FF9F43",
        "topics": [
            {"id": "t3", "title": "Logical & Conditional Functions", "subtopics": [
                {"id": "s7", "text": "IF function basics"},
                {"id": "s8", "text": "IF with AND / OR functions"},
                {"id": "s9", "text": "SUMIF, COUNTIF, AVERAGEIF"},
                {"id": "s10", "text": "IFS function (multi-conditions)"},
            ]},
            {"id": "t4", "title": "Text & Date Functions", "subtopics": [
                {"id": "s11", "text": "TRIM, LEN, CONCATENATE, TEXTJOIN"},
                {"id": "s12", "text": "LEFT, RIGHT, MID, TEXTSPLIT"},
                {"id": "s13", "text": "DATE, TODAY, EOMONTH, YEARFRAC"},
            ]},
            {"id": "t5", "title": "Lookup & Reference", "subtopics": [
                {"id": "s14", "text": "VLOOKUP & HLOOKUP"},
                {"id": "s15", "text": "XLOOKUP (modern Excel)"},
                {"id": "s16", "text": "INDEX & MATCH combination"},
                {"id": "s17", "text": "CHOOSE & OFFSET"},
            ]},
        ]
    },
    {
        "id": "p3", "label": "Phase 3", "title": "Presentation & Visuals", "color": "#54A0FF",
        "topics": [
            {"id": "t6", "title": "Advanced Formatting", "subtopics": [
                {"id": "s18", "text": "Excel Tables (Ctrl+T)"},
                {"id": "s19", "text": "Conditional Formatting"},
                {"id": "s20", "text": "Data Validation & cell protection"},
            ]},
            {"id": "t7", "title": "Data Visualization", "subtopics": [
                {"id": "s21", "text": "Line, Pie, Bar/Column charts"},
                {"id": "s22", "text": "Histograms & Box-and-Whisker"},
                {"id": "s23", "text": "Sparklines in cells"},
            ]},
        ]
    },
    {
        "id": "p4", "label": "Phase 4", "title": "Advanced Analytics", "color": "#A29BFE",
        "topics": [
            {"id": "t8", "title": "Pivot Tables & Charts", "subtopics": [
                {"id": "s24", "text": "Aggregate, filter & summarize data"},
                {"id": "s25", "text": "Group data & percentage of totals"},
                {"id": "s26", "text": "Slicers & Timelines dashboards"},
            ]},
            {"id": "t9", "title": "What-If Analysis", "subtopics": [
                {"id": "s27", "text": "Scenario Manager, Goal Seek, Data Tables"},
                {"id": "s28", "text": "Analysis ToolPak add-in"},
                {"id": "s29", "text": "PMT, NPV, XNPV, XIRR"},
            ]},
        ]
    },
    {
        "id": "p5", "label": "Phase 5", "title": "Data Engineering", "color": "#00D2D3",
        "topics": [
            {"id": "t10", "title": "Power Query (ETL)", "subtopics": [
                {"id": "s30", "text": "Extract, Transform, Load automation"},
                {"id": "s31", "text": "Folder ingestion & row limit bypass"},
                {"id": "s32", "text": "Append & merge (joins)"},
                {"id": "s33", "text": "M Language & Advanced Editor"},
            ]},
            {"id": "t11", "title": "Power Pivot & DAX", "subtopics": [
                {"id": "s34", "text": "Build table relationships (one-to-many)"},
                {"id": "s35", "text": "DAX Explicit Measures"},
                {"id": "s36", "text": "Calculated Columns"},
            ]},
        ]
    },
    {
        "id": "p6", "label": "Phase 6", "title": "Application", "color": "#1DD1A1",
        "topics": [
            {"id": "t12", "title": "Portfolio Projects", "subtopics": [
                {"id": "s37", "text": "Interactive protected dashboard"},
                {"id": "s38", "text": "Dynamic charts + pivot + slicers"},
                {"id": "s39", "text": "Share on LinkedIn & GitHub"},
            ]},
        ]
    },
]

def get_all_ids():
    ids = []
    for phase in MINDMAP_DATA:
        ids.append(phase["id"])
        for topic in phase["topics"]:
            ids.append(topic["id"])
            for sub in topic["subtopics"]:
                ids.append(sub["id"])
    return ids

ALL_IDS = get_all_ids()
TOTAL = len(ALL_IDS)

def make_checkbox(item_id, label, color, completed, size="sm", strikethrough=False):
    checked = item_id in completed
    style = {
        "textDecoration": "line-through" if (checked and strikethrough) else "none",
        "color": "#888" if checked else "#ddd",
        "fontSize": "13px" if size == "sm" else "15px",
        "fontWeight": "600" if size == "md" else "normal",
    }
    box_style = {
        "width": "18px", "height": "18px", "minWidth": "18px",
        "border": f"2px solid {color if checked else '#555'}",
        "borderRadius": "5px",
        "background": color if checked else "transparent",
        "cursor": "pointer",
        "display": "flex", "alignItems": "center", "justifyContent": "center",
        "fontSize": "11px", "color": "#fff",
        "transition": "all 0.2s",
    }
    return html.Div([
        html.Div("✓" if checked else "", id={"type": "checkbox", "id": item_id},
                 style=box_style, n_clicks=0),
        html.Span(label, style=style)
    ], style={"display": "flex", "alignItems": "flex-start", "gap": "10px", "cursor": "pointer",
              "padding": "4px 6px", "borderRadius": "6px",
              "background": f"{color}18" if checked else "transparent"})

def build_layout(completed):
    total_done = sum(1 for i in ALL_IDS if i in completed)
    pct = round((total_done / TOTAL) * 100)

    phase_cards = []
    for phase in MINDMAP_DATA:
        color = phase["color"]
        phase_ids = [t["id"] for t in phase["topics"]] + [s["id"] for t in phase["topics"] for s in t["subtopics"]]
        phase_done = sum(1 for i in phase_ids if i in completed)
        phase_total = len(phase_ids)
        bar_pct = round((phase_done / phase_total) * 100) if phase_total else 0

        topic_rows = []
        for topic in phase["topics"]:
            sub_rows = []
            for sub in topic["subtopics"]:
                sub_rows.append(
                    html.Div(make_checkbox(sub["id"], sub["text"], color, completed, "sm", True),
                             style={"marginLeft": "28px", "marginBottom": "4px"})
                )
            topic_rows.append(html.Div([
                make_checkbox(topic["id"], topic["title"], color, completed, "md", True),
                html.Div(sub_rows, style={"marginTop": "6px"})
            ], style={"marginBottom": "12px", "paddingLeft": "8px",
                      "borderLeft": f"2px solid {color}44"}))

        card = dbc.Card([
            dbc.CardHeader([
                html.Div([
                    html.Div([
                        make_checkbox(phase["id"], "", color, completed, "md"),
                        html.Div([
                            html.Span(phase["label"], style={"fontSize": "10px", "letterSpacing": "2px",
                                                              "color": color, "textTransform": "uppercase"}),
                            html.Div(phase["title"], style={"fontWeight": "700", "color": "#fff", "fontSize": "15px"}),
                        ])
                    ], style={"display": "flex", "alignItems": "center", "gap": "10px"}),
                    html.Span(f"{phase_done}/{phase_total}", style={"fontSize": "12px", "color": "#888"})
                ], style={"display": "flex", "justifyContent": "space-between", "alignItems": "center"}),
                html.Div([
                    html.Div(style={"height": "3px", "background": color,
                                    "width": f"{bar_pct}%", "borderRadius": "2px",
                                    "transition": "width 0.4s"})
                ], style={"height": "3px", "background": "#222", "borderRadius": "2px",
                          "marginTop": "10px"}),
            ], style={"background": f"{color}11", "border": "none", "padding": "14px 16px"}),
            dbc.CardBody(topic_rows, style={"padding": "16px", "background": "#0d0d15"}),
        ], style={"border": f"1.5px solid {color}33", "borderRadius": "12px",
                  "overflow": "hidden", "marginBottom": "0"})
        phase_cards.append(card)

    return html.Div([
        # Header
        html.Div([
            html.Div([
                html.Div("Learning Tracker", style={"fontSize": "10px", "letterSpacing": "4px",
                                                     "color": "#888", "textTransform": "uppercase", "marginBottom": "4px"}),
                html.H1("Excel Mastery Mind Map", style={"margin": 0, "fontSize": "24px",
                                                          "fontWeight": "700", "color": "#fff", "letterSpacing": "-0.5px"}),
            ]),
            html.Div([
                html.Div([
                    html.Div("Overall Progress", style={"fontSize": "10px", "letterSpacing": "2px",
                                                         "color": "#888", "textTransform": "uppercase"}),
                    html.Div([
                        html.Span(f"{pct}", style={"fontSize": "36px", "fontWeight": "700", "color": "#fff"}),
                        html.Span("%", style={"fontSize": "16px", "color": "#888"}),
                    ]),
                    html.Div(f"{total_done} / {TOTAL} topics completed",
                             style={"fontSize": "11px", "color": "#666"}),
                ], style={"textAlign": "right"}),
                html.Div([
                    dcc.Graph(
                        figure={
                            "data": [
                                {"type": "pie", "values": [pct, 100 - pct],
                                 "hole": 0.75,
                                 "marker": {"colors": ["#54A0FF", "#1a1a2e"]},
                                 "hoverinfo": "none", "textinfo": "none"}
                            ],
                            "layout": {
                                "margin": {"t": 0, "b": 0, "l": 0, "r": 0},
                                "showlegend": False, "paper_bgcolor": "rgba(0,0,0,0)",
                                "plot_bgcolor": "rgba(0,0,0,0)", "height": 70, "width": 70,
                            }
                        },
                        config={"displayModeBar": False},
                        style={"height": "70px", "width": "70px"}
                    )
                ])
            ], style={"display": "flex", "alignItems": "center", "gap": "16px"})
        ], style={"display": "flex", "justifyContent": "space-between", "alignItems": "center",
                  "padding": "24px 32px", "borderBottom": "1px solid #222",
                  "background": "#0a0a0f", "flexWrap": "wrap", "gap": "12px"}),

        # Phase grid
        html.Div([
            html.Div(phase_cards[:3], style={"display": "flex", "flexDirection": "column", "gap": "16px", "flex": 1}),
            html.Div(phase_cards[3:], style={"display": "flex", "flexDirection": "column", "gap": "16px", "flex": 1}),
        ], style={"display": "flex", "gap": "20px", "padding": "28px 32px",
                  "background": "#0a0a0f", "minHeight": "calc(100vh - 120px)", "flexWrap": "wrap"}),
    ])


app.layout = html.Div([
    dcc.Store(id="completed-store", data=[], storage_type="local"),
    html.Div(id="main-content"),
])


@app.callback(
    Output("main-content", "children"),
    Input("completed-store", "data"),
)
def render_page(completed_list):
    completed = set(completed_list or [])
    return build_layout(completed)


@app.callback(
    Output("completed-store", "data"),
    Input({"type": "checkbox", "id": ALL}, "n_clicks"),
    State("completed-store", "data"),
    prevent_initial_call=True,
)
def toggle_item(n_clicks_list, completed_list):
    ctx = callback_context
    if not ctx.triggered:
        return completed_list
    triggered = ctx.triggered[0]["prop_id"]
    item_id = json.loads(triggered.split(".")[0])["id"]
    completed = set(completed_list or [])
    if item_id in completed:
        completed.discard(item_id)
    else:
        completed.add(item_id)
    return list(completed)


if __name__ == "__main__":
    app.run(debug=True)
