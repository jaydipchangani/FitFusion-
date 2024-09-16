import streamlit as st
import matplotlib.pyplot as plt

st.markdown("""
    <style>
    .stButton button {
        background-color: transparent;
        color: white;
        border: none;
        padding: 8px 16px;
        font-size: 16px;
        font-weight: bold;
        cursor: pointer;
    }

    .card {
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
        transition: 0.3s;
        background-color: red;
    }
    .card:hover {
        box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2);
    }

    .hero {
        background-color: #f7f7f7;
        padding: 2px;
        text-align: center;
    }
   
    .team-photo {
        width: 150px;
        height: 150px;
        border-radius: 5%;
        object-fit: cover;
        margin-bottom: 15px;
    }
    .team-name {
        font-size: 20px;
        font-weight: bold;
        margin-bottom: 5px;
    }
    .team-role {
        font-size: 16px;
        color: grey;
    }


    </style>
    """, unsafe_allow_html=True)

if st.sidebar.button("Home"):

    st.markdown("<h1 style='text-align: center;'>FitFusion</h1>", unsafe_allow_html=True)
    st.write("")
    
    st.markdown("<h3 style='text-align: center;'>A Data Driven Approach to Optimal Health and Performance</h3>", unsafe_allow_html=True)


    st.markdown("<section class='hero'>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'>Why Choose FitFusion?</h2>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("<h3>Personalized Nutrition Plans</h3>", unsafe_allow_html=True)
        st.write("Get customized nutrition plans based on your goals and preferences.")

    with col2:
        st.markdown("<h3>Data-Driven Fitness Tracking</h3>", unsafe_allow_html=True)
        st.write("Track your progress and make data-driven decisions to optimize your fitness journey.")

    with col3:
        st.markdown("<h3>Personalized Expert Guidance</h3>", unsafe_allow_html=True)
        st.write("Get guidance from certified nutritionists and fitness experts to help you achieve your goals.")
    st.markdown("</section>", unsafe_allow_html=True)
    st.markdown("<section class='hero'>", unsafe_allow_html=True)

    st.markdown("<h2 style='text-align: center;'>Three Musketeers </h2>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)

# Card 1: Team member 1
    with col1:
        st.markdown('<img src="https://media-bom2-1.cdn.whatsapp.net/v/t61.24694-24/309218703_609632740934085_4199115356083855379_n.jpg?ccb=11-4&oh=01_Q5AaIMLjNgENAwFYqfIQCDsp0NXHcquxscXpOFKdTjeSUezN&oe=66F01741&_nc_sid=5e03e0&_nc_cat=107" class="team-photo">', unsafe_allow_html=True)
        st.markdown('<div class="team-name">Jay Gandhi</div>', unsafe_allow_html=True)
        st.markdown('<div class="team-role">An Engineer</div>', unsafe_allow_html=True)

# Card 2: Team member 2
    with col2:
        st.markdown('<img src="https://static.wixstatic.com/media/ec3afe_f910b3fbc64d4b4f9ffcce6b2a9ceb41~mv2.jpeg/v1/crop/x_58,y_11,w_606,h_606/fill/w_480,h_480,al_c,q_80,usm_0.66_1.00_0.01,enc_auto/jaydip_image.jpeg" class="team-photo">', unsafe_allow_html=True)
        st.markdown('<div class="team-name">Jaydip Changani</div>', unsafe_allow_html=True)
        st.markdown('<div class="team-role">An Engineer</div>', unsafe_allow_html=True)

# Card 3: Team member 3
    with col3:

        st.markdown('<img src="https://media-bom2-1.cdn.whatsapp.net/v/t61.24694-24/455815147_522708773640901_2108772435074668217_n.jpg?ccb=11-4&oh=01_Q5AaIJ9DFii3lJ1Vr01PrDub6zzM-Tij7zGa1077AWOw_vaa&oe=66F013AE&_nc_sid=5e03e0&_nc_cat=101" class="team-photo">', unsafe_allow_html=True)
        st.markdown('<div class="team-name">Fenil Nasriwala</div>', unsafe_allow_html=True)
        st.markdown('<div class="team-role">An Engineer</div>', unsafe_allow_html=True)


if st.sidebar.button("Diet Recommendation"):
    st.write("### Diet Recommendation")


if st.sidebar.button("Custom Food Recommendation"):
    st.write("### Custom Food Recommendation")
    st.header("Nutrients in Chocolate")

# Define the data for the pie chart
    labels = ['Fat', 'Carbohydrates', 'Protein', 'Fiber', 'Sugar']
    sizes = [35, 45, 10, 5, 5]
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc00', '#663300']

# Create the pie chart
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # Display the pie chart
    st.pyplot(fig)


if st.sidebar.button("Medical Report"):
    st.write("### Medical Report")


if st.sidebar.button("Fitness Recommendatoin"):
    st.write("### Fitness Recommendatoin")
                                  