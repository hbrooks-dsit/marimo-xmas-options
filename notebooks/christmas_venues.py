import marimo

__generated_with = "0.16.2"
app = marimo.App(width="medium", css_file="./christmas-theme.css")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(
        """
    # 🎄 Christmas Venue Options Around Manchester 🎄

    Help us choose the perfect venue for our Christmas celebration!!
    """
    )
    return


@app.cell
def _(mo):
    # Add some festive background music
    # Note: When downloading as HTML, make sure to copy the 'data' folder 
    # to the same location as the HTML file for audio to work
    try:
        audio_widget = mo.audio("./data/christmas-wrapping.mp3")
    except Exception:
        # Fallback if audio file is not found
        audio_widget = mo.md("🎵 *Audio file not available")
    
    mo.vstack([
        mo.md("🎵 **Festive Background Music** 🎵"),
        audio_widget
    ])
    return


@app.cell
def _():
    # Define venue options
    venues = [
        {
            "name": "Black Friars",
            "location": "Salford",
            "description": "Historic pub with traditional atmosphere, great food and festive decorations",
            "features": ["Private dining area", "Christmas menu", "Historic setting", "Good transport links"],
            "price": "2 Courses: £38, 3 Courses: £45",
            "menu_image": "https://theblackfriarsalford.co.uk/wp-content/uploads/2025/08/FESTIVE-MENU-2025.png",
            "vegan_menu_image": "https://theblackfriarsalford.co.uk/wp-content/uploads/2025/09/2.png"
        },
        {
            "name": "Tariff and Dale",
            "location": "Manchester, Northern Quarter",
            "description": "Contemporary restaurant with seasonal British cuisine and festive atmosphere",
            "features": ["Christmas menu", "Modern British cuisine", "Central location", "Seasonal ingredients"],
            "price": "2 Courses: £34, 3 Courses: £39",
            "menu_images": ["data/t&d-menu-1.jpg", "data/t&d-menu-2.jpg"],
            "vegan_menu_image": ""
        },
        {
            "name": "Trof NQ",
            "location": "Manchester, Northern Quarter",
            "description": "Three-floor venue with exposed brick, cosy booths, and renowned for the best roast dinners in Manchester",
            "features": ["Private hire options", "Festive set course menu", "Buffet options", "Multiple floors", "Cosy booths", "Private bar", "Third story lounge"],
            "price": "Set Course: 2 Courses £30, 3 Courses £35 | Buffet: £28pp (18+ people)",
            "menu_images": ["https://trofnq.co.uk/wp-content/uploads/2025/09/CHRISTMAS-MENU-FOOD-1-scaled.png"],
            "vegan_menu_image": ""
        }
    ]
    return (venues,)


@app.cell
def _(mo, venues):
    # Display all venues
    venue_cards = []

    for venue in venues:
        features_list = "\n".join([f"• {feature}" for feature in venue["features"]])
        card_content = f"""
    # 🍽️ **{venue['name'].upper()}** 🍽️
    ## 📍 {venue['location']}

    **{venue['description']}**

    💰 **Price:** {venue['price']}

    🎯 **Features:**
    {features_list}
    ---
    """

        # Create menu images/links
        menu_items = {}

        # Handle single menu image
        if venue.get("menu_image"):
            if venue["menu_image"].endswith('.pdf'):
                menu_items["Christmas Menu (PDF)"] = mo.md(f'[View Christmas Menu]({venue["menu_image"]})')
            elif venue["menu_image"].startswith('http'):
                # Remote image - use markdown
                menu_items["Christmas Menu"] = mo.md(f'![Christmas Menu]({venue["menu_image"]})')
            else:
                # Local image - use mo.image()
                menu_items["Christmas Menu"] = mo.image(venue["menu_image"])

        # Handle multiple menu images
        if venue.get("menu_images"):
            for i, image_path in enumerate(venue["menu_images"], 1):
                menu_items[f"Christmas Menu - Page {i}"] = mo.image(image_path)

        if venue["vegan_menu_image"]:
            if venue["vegan_menu_image"].startswith('http'):
                menu_items["Vegan Menu"] = mo.md(f'![Vegan Menu]({venue["vegan_menu_image"]})')
            else:
                menu_items["Vegan Menu"] = mo.image(venue["vegan_menu_image"])

        menu_carousel = mo.accordion(menu_items) if menu_items else mo.md("No menu available")

        venue_card = mo.vstack([
            mo.md(card_content),
            mo.md("#### Menus:"),
            menu_carousel
        ])
        venue_cards.append(venue_card)

    mo.vstack(venue_cards)
    return


if __name__ == "__main__":
    app.run()
