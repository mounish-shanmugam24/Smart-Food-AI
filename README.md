# Smart-Food-AI

**An AI-powered nutrition and food assistant that helps people make healthier everyday food choices.**

Smart Food AI brings four tools together in one web app: it analyses nutrition labels and food photos, detects how a meal was cooked, generates recipes that are read aloud, and finds nearby restaurants on a live map. It is built with Python and Streamlit, uses Google Cloud AI services, and was containerised with **Docker** and deployed on **Google Cloud**.

> ℹ️ The live demo is no longer online because the Google Cloud access used for deployment was time-limited. The screenshots are uploaded were taken from the deployed app.

---

## 📌 Why I Built It

Making healthy food choices usually means juggling several apps: one to read labels, one for recipes, one to find places to eat. Nutrition labels are also hard to interpret quickly. Smart Food AI puts these tasks in one place and uses AI to turn photos and plain-language requests into clear, practical health guidance.

---

## 🧭 App Overview

The app is a multi-page Streamlit application. A sidebar lets users switch between four modules, each with its own colour theme.


| Module | What it does |
|--------|--------------|
| 🟦 **Nutrition Mode** | Upload a food photo or nutrition label for instant calorie, macro and health analysis |
| 🟨 **AI Chef** | Generate a recipe for any dish, tailored to dietary preferences, and have it read aloud |
| 🟧 **Food Analyzer** | Upload a meal photo to detect the dish, cooking method and portion size, with a health verdict |
| 🟥 **Restaurant Finder** | Find food options in any area, shown on a live map with ratings and directions |

---

## 🔍 Features in Detail

### 1. 🟦 Nutrition Analyzer
Upload a photo of a meal or a **nutrition label** (JPG, JPEG or PNG). The AI reads the image and returns a structured health analysis:

- **Estimated calories:** per serving, with practical context (for example, a pouch of two pastries doubles the calories)
- **Macro breakdown:** protein, carbohydrates (including sugar and fibre) and fats (including saturated fat)
- **Health rating:** an overall verdict such as *Poor*, with the reasoning behind it
- **Hidden risks:** warnings such as high sugar content from multiple sources (sugar, corn syrup, dextrose)

*Example: a Kellogg's Pop-Tarts label was analysed as 210 calories per pastry, 34g carbohydrates including 12g sugar, and rated "Poor" because it is highly processed and low in fibre and protein.*



### 2. 🟨 Voice-Activated AI Chef
Type what you want to cook and choose a **dietary preference**:
- None
- Vegetarian
- High Protein
- Low Carb

The AI Chef generates a **concise, step-by-step recipe**, then converts it to speech with **Google Cloud Text-to-Speech**. A built-in audio player lets users listen to the instructions while they cook, hands-free.

*Example: "Chicken Biryani" returns five clear steps (marinate, cook the chicken base, par-cook the rice, layer, dum cook) plus an audio version.*


### 3. 🟧 Food Diagnostics Analyzer
Upload a photo of a plated meal and click **Run Deep Scan**. The AI identifies:

- **Detected dish:** what the meal is
- **Likely cooking method:** for example grilled, fried or steamed, which strongly affects how healthy a meal is
- **Portion size:** small, medium or large
- **Verdict:** an overall health assessment, such as *Balanced*

*Example: a photo of fish with vegetables was detected as "Grilled Fish with Sautéed Vegetables", medium portion, with a "Balanced" verdict.*


### 4. 🟥 Smart Restaurant Finder
Enter an **area** (for example, Edgbaston, Birmingham) and **what you're craving** (for example, South Indian restaurant), then click **Search Live Map**. The app shows:

- An **interactive area map** with every result marked
- A **Top Results** list with each restaurant's name, **star rating** and full address
- A **Get Directions** button that opens the route to the restaurant

*Example: searching "South Indian restaurant" in Edgbaston returned nearby options with ratings from 4.4 to 4.6, each with one-click directions.*


## ⚙️ How It Works

```
                    ┌──────────────────────────────┐
                    │   Streamlit multi-page app   │
                    └──────────────┬───────────────┘
        ┌──────────────┬───────────┴───────┬──────────────────┐
        ▼              ▼                   ▼                  ▼
  Nutrition Mode    AI Chef         Food Analyzer     Restaurant Finder
  (image upload)  (text + diet)     (image upload)    (area + craving)
        │              │                   │                  │
        ▼              ▼                   ▼                  ▼
  Google Cloud    AI recipe  ──►     Google Cloud       Google Maps /
  AI vision       generation   Text-to-Speech  AI vision     Places API
        │              │        (audio)    │                  │
        ▼              ▼                   ▼                  ▼
  Calories, macros, Step-by-step     Dish, cooking      Live map, ratings,
  rating, risks    recipe + audio    method, portion,   addresses,
                                     verdict            directions
```

1. The user picks a module from the sidebar.
2. Images and text inputs are sent to Google Cloud AI services for analysis or generation.
3. Responses are formatted into clear sections (calories, macros, risks, verdicts, recipe steps).
4. For the AI Chef, the recipe text is converted to audio with Text-to-Speech and played in the app.
5. For the Restaurant Finder, location results are plotted on an interactive map with ratings and directions links.

---

## 🛠️ Tech Stack

| Area | Technology |
|------|------------|
| Language | Python |
| Web app | Streamlit (multi-page app with sidebar navigation) |
| Image understanding | Google Cloud Vision API |
| Speech | Google Cloud Text-to-Speech |
| Location & maps | Google Maps / Places API |
| Containerisation | Docker |
| Deployment | Docker container deployed on Google Cloud |

---

## 🐳 Deployment

The application is packaged as a **Docker** container, which bundles the app, its Python dependencies and its configuration into one image. This kept the app consistent between local development and the cloud, and made it straightforward to deploy on Google Cloud. API keys were supplied as environment variables at runtime and never stored in the code or the image.

The hosted version was available for a limited period using time-limited Google Cloud access, and is no longer live. Because the app is containerised, it can be redeployed to any Docker-compatible platform.

---

## 🧩 Limitations & Future Improvements

- Calorie and portion estimates from photos are approximate and are not a substitute for professional dietary advice.
- Add **speech-to-text input** to the AI Chef so users can ask for recipes by voice.
- Let users **save meals** and track daily nutrition over time.
- Add **allergen detection** (for example nuts, gluten or dairy) to the label and photo analysis.
- Filter the Restaurant Finder by dietary needs, such as vegetarian or low-carb options.

---

## ⚠️ Disclaimer

Smart Food AI provides general nutrition information for educational purposes only. It is not medical or dietary advice.

---

## 👤 Author

**Mounish Shanmugam**
MSc Artificial Intelligence & Machine Learning, University of Birmingham
[LinkedIn](https://www.linkedin.com/in/mounish-shanmugam-5a4590233) · [GitHub]([https://github.com/<your-username>](https://github.com/mounish-shanmugam24))
