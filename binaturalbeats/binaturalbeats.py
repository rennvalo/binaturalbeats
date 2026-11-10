import os
import reflex as rx
from starlette.staticfiles import StaticFiles


def parallax_section(content: rx.Component, height: str = "100vh") -> rx.Component:
    """Render a full-width hero section over the page background."""
    return rx.box(
        rx.box(
            content,
            width="100%",
            max_width="1200px",
            margin="0 auto",
            padding="2em 1em",
            display="flex",
            flex_direction="column",
            justify_content="center",
            align_items="center",
            min_height=height,
            position="relative",
        ),
        style={
            "background_color": "rgba(0, 0, 0, 0.2)",
            "position": "relative",
            "width": "100%",
            "min_height": height,
        },
    )


# State management
class State(rx.State):
    """The app state."""
    # Contact form state
    name: str = ""
    email: str = ""
    message: str = ""
    submitted: bool = False

    def handle_submit(self, form_data: dict):
        self.name = form_data.get("name", "")
        self.email = form_data.get("email", "")
        self.message = form_data.get("message", "")
        self.submitted = True

    def reset_form(self):
        self.name = ""
        self.email = ""
        self.message = ""
        self.submitted = False


def navigation_bar() -> rx.Component:
    """Header navigation component."""
    return rx.hstack(
        rx.hstack(
            rx.heading("Bi Natural Beats Binural Audio Tracks", size="5", font_weight="bold", color="#1a202c"),
            align="center",
        ),
        rx.spacer(),
        rx.hstack(
            rx.link(
                rx.button("Home", variant="solid", color_scheme="gray"),
                href="/",
            ),
            rx.link(
                rx.button("Book", variant="solid", color_scheme="teal"),
                href="/book",
            ),
            spacing="3",
            align="center",
        ),
        width="100%",
        max_width="1200px",
        padding_y="1.5em",
        padding_x="1em",
        border_bottom="1px solid #e2e8f0",
        align="center",
    )


def footer() -> rx.Component:
    """Footer component."""
    return rx.vstack(
        rx.text("© Bi Natural Beats Studio - Colorado Outdoor Sound Lab", font_size="0.9em", color="#718096"),
        rx.hstack(
            rx.link("Privacy Policy", href="/privacy", color="#4a5568"),
            rx.text("·", color="#a0aec0"),
            rx.link("Terms of Service", href="/terms", color="#4a5568"),
            spacing="2",
            justify="center",
        ),
        rx.text("Crafted with Reflex & Python", font_size="0.8em", color="#a0aec0"),
        spacing="2",
        align="center",
        padding_y="3em",
        width="100%",
        border_top="1px solid #e2e8f0",
        margin_top="4em",
        background="rgba(255, 255, 255, 0.88)",
        border_radius="16px",
    )


def track_card(title: str, audio_url: str, image_url: str = None, subtitle: str = None, description: str = None) -> rx.Component:
    """Helper to render an audio track card with player and artwork."""
    return rx.box(
        rx.vstack(
            rx.heading(title, size="4", font_weight="bold", color="#2d3748"),
            rx.cond(
                image_url is not None,
                rx.image(
                    src=image_url if image_url else "",
                    width="100%",
                    max_width="600px",
                    height="auto",
                    border_radius="10px",
                    alt=title,
                    box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
                ),
            ),
            rx.cond(
                subtitle is not None,
                rx.text(subtitle if subtitle else "", font_size="0.9em", color="#718096", italic=True),
            ),
            rx.box(
                rx.audio(
                    url=audio_url,
                    controls=True,
                    width="100%",
                ),
                width="100%",
                max_width="600px",
                padding_y="0.5em",
            ),
            rx.cond(
                description is not None,
                rx.text(
                    description if description else "",
                    font_size="0.95em",
                    text_align="center",
                    color="#4a5568",
                    max_width="600px",
                ),
            ),
            spacing="3",
            align="center",
            width="100%",
        ),
        padding="1.5em",
        background="#ffffff",
        border_radius="12px",
        box_shadow="0 1px 3px 0 rgba(0, 0, 0, 0.1)",
        width="100%",
        max_width="650px",
    )


def index() -> rx.Component:
    """Home / Index Page matching the full WordPress design."""
    return rx.center(
        rx.vstack(
            parallax_section(
                rx.vstack(
                    navigation_bar(),
                    rx.badge("1–8 Hz", color_scheme="teal", variant="surface", size="2"),
                    rx.text("Brought to you", font_size="1.25em", text_align="center", color="#ffffff"),
                    rx.heading("Bi Natural Beats Studio", size="8", text_align="center", font_weight="extrabold", color="#ffffff"),
                    rx.heading("We are an independent creative outdoor recording studio", size="5", text_align="center", color="#e2e8f0", font_weight="medium"),
                    spacing="3",
                    align="center",
                    padding_y="2em",
                    max_width="800px",
                ),
                height="80vh",
            ),
            
            # Cover Image
            rx.box(
                rx.image(
                    src="/media/images/cover.png", 
                    width="100%", 
                    height="auto", 
                    border_radius="16px",
                    alt="Cover Image",
                    box_shadow="0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)",
                ),
                width="100%",
                max_width="900px",
                padding_x="1em",
            ),

            # Intro Section
            rx.vstack(
                rx.heading("Bi Natural Beats", size="6", text_align="center", font_weight="bold"),
                rx.text(
                    "We are a small recording studio based in Colorado focused on combining natural sounds with Binaural Beats to achieve altered states of consciousness and creating high levels of concentration, focused activity, meditation, relaxation, and lucid dream states.",
                    text_align="center",
                    font_size="1.1em",
                    max_width="800px",
                    line_height="1.75",
                    color="#4a5568",
                ),
                spacing="4",
                align="center",
                padding_y="3em",
                padding_x="1em",
                background="rgba(255, 255, 255, 0.88)",
                border_radius="16px",
                width="100%",
            ),

            # Audio Gallery Section
            rx.vstack(
                rx.heading("Soundscapes & Field Recordings", size="6", font_weight="bold", color="#2d3748"),
                rx.text("Experience raw outdoor binaural captures directly from Colorado wilderness", color="#718096"),
                
                track_card(
                    title="Industrial Birds 3D",
                    audio_url="/media/audio/221024_001_Binaural_industrial_birds-2.mp3",
                    image_url="/media/images/birds.jpg",
                ),
                
                track_card(
                    title="Industrial Birds Focused",
                    audio_url="/media/audio/221024_001_Binaural_industrial_birds-1.mp3",
                    image_url="/media/images/bird.JPG",
                    subtitle="Boulder Canyon birds",
                ),
                
                track_card(
                    title="Boulder Canyon Birds (Binaural)",
                    audio_url="/media/audio/BoulderCanyonBirds_Binaural.mp3",
                    image_url="/media/images/bird.JPG",
                    subtitle="Pure Boulder Canyon field capture",
                ),
                
                track_card(
                    title="Snow Creek near Big Elk Meadows",
                    audio_url="/media/audio/snow_creek-1.mp3",
                    image_url="/media/images/snow_creek.jpg",
                    subtitle="Snow Creek near Big Elk Meadows",
                ),

                spacing="6",
                align="center",
                width="100%",
                padding_y="2em",
                background="rgba(255, 255, 255, 0.88)",
                border_radius="16px",
            ),

            # Call to Action
            rx.box(
                rx.vstack(
                    rx.heading("Ready to immerse in natural acoustics?", size="6", text_align="center", color="#1a202c"),
                    rx.text("Connect with our studio team for custom audio productions or licensing.", color="#4a5568", text_align="center"),
                    rx.link(
                        rx.button(
                            "Connect With Us", 
                            variant="surface",
                            color_scheme="teal",
                            size="3",
                        ),
                        href="/contact",
                    ),
                    spacing="4",
                    align="center",
                ),
                padding="4em 2em",
                background="#f7fafc",
                border_radius="16px",
                width="100%",
                max_width="900px",
                border="1px solid #e2e8f0",
                margin_y="2em",
            ),

            footer(),
            
            width="100%",
            spacing="8",
            align="center",
        ),
        width="100%",
        min_height="100vh",
        style={
            "background_image": "url('/media/images/background.jpg')",
            "background_attachment": "fixed",
            "background_position": "center",
            "background_repeat": "no-repeat",
            "background_size": "cover",
        },
    )


def page_layout(content: rx.Component) -> rx.Component:
    """Render a standard page over the site's fixed background image."""
    return rx.center(
        rx.vstack(
            navigation_bar(),
            content,
            footer(),
            width="100%",
            max_width="1200px",
            spacing="6",
            align="center",
            padding_x="1em",
        ),
        width="100%",
        min_height="100vh",
        style={
            "background_image": "url('/media/images/background.jpg')",
            "background_attachment": "fixed",
            "background_position": "center",
            "background_repeat": "no-repeat",
            "background_size": "cover",
        },
    )


def book() -> rx.Component:
    """Dedicated album and companion book page."""
    return page_layout(
        rx.vstack(
            rx.heading("Nature is Binaural", size="7", text_align="center", font_weight="bold", color="#1a202c"),
            rx.image(
                src="/media/images/cover-small.png",
                width="100%",
                max_width="600px",
                border_radius="15px",
                alt="Nature is Binaural album cover",
                box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1)",
            ),
            rx.text(
                "Introducing Bi Natural Beats, a unique album that combines the beauty of nature with binaural beats. Our tracks are carefully crafted using real-life recordings from the Rocky Mountains and specifically tuned brain waves to achieve a range of desired states of consciousness.",
                font_weight="medium",
                text_align="center",
                max_width="800px",
                font_size="1.1em",
                line_height="1.75",
                color="#4a5568",
                padding_x="1em",
            ),
            rx.vstack(
                track_card(
                    title="Rockin Robin",
                    audio_url="/media/audio/RockinRobn.mp3",
                    image_url="/media/images/birds.jpg",
                    description="Track 1, Rockin' Robbin, is perfect for your daily tasks. It's tuned to 741 hz to promote problem-solving and puts your brain into beta. This track features the sounds of local birds in Boulder, CO.",
                ),
                track_card(
                    title="Awakened",
                    audio_url="/media/audio/11_awakened.mp3",
                    image_url="/media/images/awkaend.jpg",
                    description="Track 2, Awakened, is a special recording of Elk bugling all night in Rocky Mountain National Park. This track is tuned to 852 hz to promote returning to spiritual order.",
                ),
                track_card(
                    title="Rainy Daze",
                    audio_url="/media/audio/12_ranydaze.mp3",
                    image_url="/media/images/rainy.jpg",
                    description="Track 3, Rainy Daze, is a soothing and relaxing track recorded on a rainy evening in the Rocky Mountains. It's tuned to 396 hz to promote the release of fear, guilt, and anxiety.",
                ),
                track_card(
                    title="Sleepy Elk",
                    audio_url="/media/audio/13_sleepyElk-1.mp3",
                    image_url="/media/images/sleepy-elk.jpg",
                    description="Track 4, Sleepy Elk, is the perfect way to end your day. It's tuned to 174 Hz to promote deep relaxation, slowly bringing your brain from Alpha to Delta.",
                ),
                spacing="6",
                width="100%",
                align="center",
            ),
            rx.link(
                rx.button("Download Rocky Mountain Book (PDF)", color_scheme="blue", size="3"),
                href="/media/docs/RockyMountainBook.pdf",
                is_external=True,
            ),
            spacing="6",
            align="center",
            width="100%",
            max_width="900px",
            padding_y="2em",
            background="rgba(255, 255, 255, 0.88)",
            border_radius="16px",
        )
    )


def legal_section(title: str, body: str) -> rx.Component:
    """Render one readable section on a legal information page."""
    return rx.vstack(
        rx.heading(title, size="4", color="#1a202c"),
        rx.text(body, color="#4a5568", line_height="1.7"),
        spacing="2",
        align="start",
        width="100%",
    )


def privacy_policy() -> rx.Component:
    """Provide a plain-language privacy notice for the current site."""
    return page_layout(
        rx.vstack(
            rx.heading("Privacy Policy", size="7", color="#1a202c"),
            rx.text("Last updated: November 6, 2026", color="#718096"),
            rx.text(
                "This notice explains how Bi Natural Beats Studio handles information when you visit this website. It is a general summary, not a guarantee of compliance with every privacy law. Please obtain legal advice for your location and circumstances.",
                color="#4a5568",
                line_height="1.7",
            ),
            legal_section(
                "Information you provide",
                "The contact form asks for your name, email address, and message. In the current site version, submitting the form displays an on-page confirmation; it is not connected to an email or inquiry-management service. Do not include sensitive or confidential information. If the form is connected to a service in the future, this policy should be updated to identify that service and explain how submissions are handled.",
            ),
            legal_section(
                "Technical information",
                "When you load this website, the hosting and network infrastructure may process technical information such as your IP address, browser and device details, requested pages, and timestamps in order to deliver, secure, and troubleshoot the site. The hosting provider's own practices may also apply.",
            ),
            legal_section(
                "Cookies, analytics, and third parties",
                "This site does not currently advertise analytics, targeted advertising, or account features. The application or hosting provider may use essential technical storage or logs. Audio, images, and the downloadable PDF are served by this website. If third-party analytics, embedded services, or advertising are added, this notice should be revised.",
            ),
            legal_section(
                "How information is used and retained",
                "Information is used to operate and protect the website and, if a working contact channel is added, to respond to inquiries. Technical logs may be retained by hosting providers according to their policies. This site does not currently describe a fixed retention schedule; avoid sending information you would not want processed by the website infrastructure.",
            ),
            legal_section(
                "Your choices and children",
                "You may choose not to use the contact form. Depending on where you live, privacy laws may give you rights to access, correct, delete, or restrict certain personal information. This site is not directed to children under 13, and we do not knowingly seek personal information from children.",
            ),
            legal_section(
                "Changes and contact",
                "This policy may be updated as the site changes. The date at the top indicates the most recent revision. The current contact form does not deliver messages to the studio, so do not rely on it for privacy requests until a monitored contact method is provided.",
            ),
            spacing="5",
            align="start",
            width="100%",
            max_width="900px",
            padding="2em",
            background="rgba(255, 255, 255, 0.92)",
            border_radius="16px",
            margin_y="2em",
        )
    )


def terms_of_service() -> rx.Component:
    """Provide basic terms for use of the website and its content."""
    return page_layout(
        rx.vstack(
            rx.heading("Terms of Service", size="7", color="#1a202c"),
            rx.text("Last updated: November 6, 2026", color="#718096"),
            rx.text(
                "By accessing this website, you agree to these terms. If you do not agree, please do not use the website. These terms are a general starting point and are not legal advice or a guarantee that every legal requirement is met.",
                color="#4a5568",
                line_height="1.7",
            ),
            legal_section(
                "Website content and permitted use",
                "The website provides studio information, audio previews, images, and a downloadable PDF. Unless a page or separate written permission says otherwise, the site's text, recordings, artwork, and other materials are owned by Bi Natural Beats Studio or its licensors. You may access the site for personal, non-commercial use; do not copy, redistribute, publicly perform, modify, or commercially exploit the materials without permission.",
            ),
            legal_section(
                "Health and safety",
                "Audio and frequency descriptions are provided for general informational and entertainment purposes only. They are not medical or mental-health advice, diagnosis, or treatment, and results vary. Consult a qualified professional about health concerns. Listen at a comfortable volume and do not use headphones or this site while driving, operating machinery, or doing anything that requires awareness of your surroundings.",
            ),
            legal_section(
                "Acceptable use",
                "Do not misuse the website, attempt to disrupt its operation or security, or use its content in a way that violates applicable law or another person's rights.",
            ),
            legal_section(
                "Availability and disclaimers",
                "The website and its content are provided on an \"as available\" basis. We do not promise uninterrupted access, error-free content, or that the site will meet every user's needs. To the extent permitted by law, implied warranties are disclaimed.",
            ),
            legal_section(
                "Limitation of liability",
                "To the extent permitted by applicable law, Bi Natural Beats Studio is not liable for indirect, incidental, special, or consequential loss arising from use of the site or its content. Nothing in these terms limits liability where applicable law does not allow it to be limited.",
            ),
            legal_section(
                "External links and changes",
                "Links to third-party websites are provided for convenience; we do not control or endorse their content or practices. We may update the website or these terms from time to time. Continued use after an update means you accept the revised terms.",
            ),
            legal_section(
                "Governing law",
                "These terms are governed by the laws of the State of Colorado, United States, without regard to conflict-of-law principles, except where applicable consumer-protection law requires otherwise.",
            ),
            legal_section(
                "Contact",
                "The current contact form is not connected to a monitored message service. Please do not rely on it to send legal notices, permissions requests, or time-sensitive communications.",
            ),
            spacing="5",
            align="start",
            width="100%",
            max_width="900px",
            padding="2em",
            background="rgba(255, 255, 255, 0.92)",
            border_radius="16px",
            margin_y="2em",
        )
    )


def contact() -> rx.Component:
    """Contact page allowing users to send messages to the studio."""
    return rx.center(
        rx.vstack(
            navigation_bar(),
            
            rx.vstack(
                rx.badge("Get in Touch", color_scheme="teal", variant="surface", size="2"),
                rx.heading("Connect With Us", size="8", font_weight="bold", color="#1a202c"),
                rx.text(
                    "Reach out to Bi Natural Beats Studio for questions about audio engineering, custom recordings, or licensing.",
                    text_align="center",
                    color="#4a5568",
                    max_width="600px",
                ),
                spacing="3",
                align="center",
                padding_y="2em",
            ),

            rx.box(
                rx.cond(
                    State.submitted,
                    rx.vstack(
                        rx.box(
                            rx.heading("Thank you for connecting!", size="5", color="#2f855a"),
                            rx.text("We received your message and will respond shortly.", color="#4a5568"),
                            padding="1.5em",
                            background="#f0fff4",
                            border="1px solid #9ae6b4",
                            border_radius="8px",
                            width="100%",
                        ),
                        rx.button("Send Another Message", on_click=State.reset_form, variant="outline", color_scheme="teal"),
                        spacing="4",
                        align="center",
                    ),
                    rx.form(
                        rx.vstack(
                            rx.vstack(
                                rx.text("Your Name", font_weight="medium", font_size="0.9em"),
                                rx.input(name="name", placeholder="John Doe", required=True, width="100%"),
                                align="start",
                                width="100%",
                            ),
                            rx.vstack(
                                rx.text("Email Address", font_weight="medium", font_size="0.9em"),
                                rx.input(name="email", type="email", placeholder="you@example.com", required=True, width="100%"),
                                align="start",
                                width="100%",
                            ),
                            rx.vstack(
                                rx.text("Message", font_weight="medium", font_size="0.9em"),
                                rx.text_area(name="message", placeholder="Tell us about your project or inquiry...", required=True, width="100%"),
                                align="start",
                                width="100%",
                            ),
                            rx.button("Send Message", type="submit", color_scheme="teal", size="3", width="100%"),
                            spacing="4",
                            width="100%",
                        ),
                        on_submit=State.handle_submit,
                        reset_on_submit=True,
                    ),
                ),
                padding="2em",
                background="#ffffff",
                border_radius="12px",
                box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
                border="1px solid #e2e8f0",
                width="100%",
                max_width="600px",
            ),

            footer(),
            width="100%",
            max_width="1200px",
            spacing="6",
            align="center",
        ),
        width="100%",
        background_color="#f8fafc",
        min_height="100vh",
    )


app = rx.App(
    theme=rx.theme(
        appearance="light",
        has_background=True,
        accent_color="teal",
    )
)

# Static media mount directly into FastAPI backend
media_dir = os.getenv("MEDIA_DIR", "/media")
if not os.path.exists(media_dir):
    media_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "media")
if os.path.exists(media_dir):
    app.api.mount("/media", StaticFiles(directory=media_dir), name="media")

app.add_page(index, route="/", title="Bi Natural Beats Studio")
app.add_page(book, route="/book", title="Nature is Binaural - Bi Natural Beats")
app.add_page(contact, route="/contact", title="Connect With Us - Bi Natural Beats")
app.add_page(privacy_policy, route="/privacy", title="Privacy Policy - Bi Natural Beats")
app.add_page(terms_of_service, route="/terms", title="Terms of Service - Bi Natural Beats")
