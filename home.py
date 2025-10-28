# ---------------------------
# Fullscreen Splash Animation with Text
# ---------------------------
video_url = "https://github.com/SSR2308/OceanSafeLM/blob/9761d751ca32b424d92cc29eba0c179d212e7127/bc8c-f169-4534-a82d-acc2fad66609.mp4?raw=true"

splash_container = st.empty()
splash_container.markdown(f"""
<div id="splash" style="
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: white;
    display: flex;
    flex-direction: column;
    justify-content: flex-end;  
    align-items: center;        
    z-index: 9999;
    animation: fadeout 1s ease 4s forwards;
    padding-bottom: 120px;       /* keeps text in place */
">
    <video autoplay muted playsinline style="
        max-width: 85%;        /* slightly larger */
        max-height: 60%;       /* slightly taller */
        margin-bottom: 30px;   /* moves video slightly lower */
    ">
        <source src="{video_url}" type="video/mp4">
        Your browser does not support the video tag.
    </video>
    <h1 style='font-family: "Brush Script MT", cursive; font-size: 7em; color: #0077be; text-shadow: 2px 2px 8px rgba(0,0,0,0.5); transform: translateX(30px);'>
        Ocean Safe
    </h1>
</div>

<style>
@keyframes fadeout {{
    to {{
        opacity: 0;
        visibility: hidden;
    }}
}}
</style>
""", unsafe_allow_html=True)
