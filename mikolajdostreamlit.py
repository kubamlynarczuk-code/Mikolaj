import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_santa_with_gift():
    # 1. Konfiguracja płótna
    # Zwróć uwagę, że funkcja st.pyplot() przyjmuje obiekt figury
    fig, ax = plt.subplots(figsize=(8, 9))
    ax.set_aspect('equal')
    ax.set_xlim(0, 11)
    ax.set_ylim(-6, 11)
    ax.axis('off')

    # Tło
    ax.set_facecolor('#87CEEB') # Niebieskie niebo
    fig.patch.set_facecolor('#87CEEB')

    # Opcjonalnie: Dodajmy śnieg na dole jako duży biały prostokąt
    snow_ground = patches.Rectangle((0, -6), 11, 2.5, color='white', zorder=-10)
    ax.add_patch(snow_ground)


    # ==================== PREZENT (Obok Mikołaja) ====================
    # Współrzędne bazowe prezentu (lewy dolny róg)
    gift_x, gift_y = 7.8, -5.5
    gift_w, gift_h = 2.2, 2.2
    ribbon_color = 'gold'
    box_color = 'forestgreen'
    gift_z = -4.5

    # 1. Główne pudełko
    box = patches.Rectangle((gift_x, gift_y), gift_w, gift_h,
                            color=box_color, ec='darkgreen', lw=1, zorder=gift_z)
    ax.add_patch(box)

    # 2. Wstążka pionowa
    ribbon_v = patches.Rectangle((gift_x + gift_w/2 - 0.2, gift_y), 0.4, gift_h,
                                 color=ribbon_color, zorder=gift_z + 0.1)
    ax.add_patch(ribbon_v)

    # 3. Wstążka pozioma
    ribbon_h = patches.Rectangle((gift_x, gift_y + gift_h/2 - 0.2), gift_w, 0.4,
                                 color=ribbon_color, zorder=gift_z + 0.1)
    ax.add_patch(ribbon_h)

    # 4. Kokarda na górze (dwie elipsy i kółko w środku)
    bow_center_x = gift_x + gift_w/2
    bow_center_y = gift_y + gift_h

    bow_left = patches.Ellipse((bow_center_x - 0.4, bow_center_y - 0.1), 0.8, 0.5, angle=30,
                               color=ribbon_color, zorder=gift_z + 0.2)
    bow_right = patches.Ellipse((bow_center_x + 0.4, bow_center_y - 0.1), 0.8, 0.5, angle=-30,
                                color=ribbon_color, zorder=gift_z + 0.2)
    bow_knot = patches.Circle((bow_center_x, bow_center_y), 0.15,
                              color=ribbon_color, ec='orange', zorder=gift_z + 0.3)

    ax.add_patch(bow_left)
    ax.add_patch(bow_right)
    ax.add_patch(bow_knot)


    # ================= CIAŁO MIKOŁAJA (Warstwy ujemne) =================
    santa_offset_x = -0.5

    # Buty
    boot_left = patches.FancyBboxPatch((2.5 + santa_offset_x, -5.5), 1.5, 2.0,
                                       boxstyle="round,pad=0.1", color='black', zorder=-5)
    boot_right = patches.FancyBboxPatch((6.0 + santa_offset_x, -5.5), 1.5, 2.0,
                                        boxstyle="round,pad=0.1", color='black', zorder=-5)
    ax.add_patch(boot_left)
    ax.add_patch(boot_right)

    # Nogi
    leg_left = patches.Rectangle((2.8 + santa_offset_x, -4.0), 1.2, 3.0, color='red', zorder=-4)
    leg_right = patches.Rectangle((6.0 + santa_offset_x, -4.0), 1.2, 3.0, color='red', zorder=-4)
    ax.add_patch(leg_left)
    ax.add_patch(leg_right)

    # Tułów
    torso = patches.Ellipse((5 + santa_offset_x, 1.5), width=6.5, height=6.0, color='red', zorder=-3)
    ax.add_patch(torso)
    coat_trim = patches.FancyBboxPatch((2.5 + santa_offset_x, -1.5), 5.0, 1.0,
                                       boxstyle="round,pad=0.2", color='white', zorder=-2.5)
    ax.add_patch(coat_trim)

    # Pas
    belt = patches.Rectangle((2.0 + santa_offset_x, 1.0), 6.0, 0.8, color='black', zorder=-2)
    buckle_outer = patches.Rectangle((4.5 + santa_offset_x, 0.8), 1.0, 1.2, color='gold', zorder=-1.5)
    buckle_inner = patches.Rectangle((4.7 + santa_offset_x, 1.0), 0.6, 0.8, color='black', zorder=-1.4)
    ax.add_patch(belt)
    ax.add_patch(buckle_outer)
    ax.add_patch(buckle_inner)

    # Ręce
    arm_left = patches.Ellipse((2.5 + santa_offset_x, 3.0), width=3.5, height=1.5, angle=30, color='red', zorder=-1)
    arm_right = patches.Ellipse((7.5 + santa_offset_x, 3.0), width=3.5, height=1.5, angle=-30, color='red', zorder=-1)
    ax.add_patch(arm_left)
    ax.add_patch(arm_right)

    # Rękawice
    mitten_left = patches.Circle((1.2 + santa_offset_x, 2.2), radius=0.7, color='black', zorder=-0.5)
    mitten_right = patches.Circle((8.8 + santa_offset_x, 2.2), radius=0.7, color='black', zorder=-0.5)
    cuff_left = patches.Circle((1.9 + santa_offset_x, 2.6), radius=0.6, color='white', zorder=-0.6)
    cuff_right = patches.Circle((8.1 + santa_offset_x, 2.6), radius=0.6, color='white', zorder=-0.6)
    ax.add_patch(mitten_left)
    ax.add_patch(mitten_right)
    ax.add_patch(cuff_left)
    ax.add_patch(cuff_right)


    # ================= GŁOWA MIKOŁAJA (Warstwy dodatnie) =================
    head_x = 5 + santa_offset_x

    # Broda
    beard_positions = [
        (head_x, 3.5, 1.2), (head_x - 1.2, 4.2, 1.0), (head_x + 1.2, 4.2, 1.0),
        (head_x - 1.8, 5.0, 0.8), (head_x + 1.8, 5.0, 0.8),
        (head_x, 2.8, 1.0), (head_x - 0.8, 3.0, 0.9), (head_x + 0.8, 3.0, 0.9)
    ]
    for x, y, r in beard_positions:
        beard = patches.Circle((x, y), radius=r, color='white', zorder=1)
        ax.add_patch(beard)

    # Twarz
    face = patches.Circle((head_x, 5.5), radius=1.3, color='#ffe0bd', zorder=2)
    ax.add_patch(face)

    # Czapka
    hat_triangle = patches.Polygon([[head_x - 2.0, 6.2], [head_x + 2.0, 6.2], [head_x, 10.2]], color='red', zorder=3)
    hat_trim = patches.FancyBboxPatch((head_x - 2.2, 6.0), 4.4, 0.8, boxstyle="round,pad=0.1", color='white', zorder=4)
    pom_pom = patches.Circle((head_x, 10.2), radius=0.6, color='white', zorder=5)
    ax.add_patch(hat_triangle)
    ax.add_patch(hat_trim)
    ax.add_patch(pom_pom)

    # Oczy i Nos
    eye_left = patches.Circle((head_x - 0.4, 5.8), radius=0.12, color='black', zorder=6)
    eye_right = patches.Circle((head_x + 0.4, 5.8), radius=0.12, color='black', zorder=6)
    nose = patches.Circle((head_x, 5.3), radius=0.25, color='#ffaaaa', zorder=6)
    ax.add_patch(eye_left)
    ax.add_patch(eye_right)
    ax.add_patch(nose)

    # Tytuł
    plt.title("Mikołaj i Prezent!", fontsize=18, color='darkgreen', fontweight='bold', y=0.95)

    return fig

# --- Główna część dla Streamlit ---
if __name__ == "__main__":
    st.set_page_config(page_title="Wesołych Świąt!", layout="centered")

    st.header("🎁 Rysunek Mikołaja w Matplotlib")
    st.markdown("Ten rysunek został stworzony wyłącznie przy użyciu bibliotek **Matplotlib** i **Matplotlib.patches**.")

    # Wywołaj funkcję rysującą i uzyskaj obiekt figury
    santa_figure = draw_santa_with_gift()

    # Wyświetl figurę w Streamlit
    st.pyplot(santa_figure)

    st.info("Aby uruchomić tę aplikację, zapisz kod jako plik np. `app.py` i uruchom w terminalu: `streamlit run app.py`")
