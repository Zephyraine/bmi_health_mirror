import streamlit as st  
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / "assets"


# =========================
# 1. 页面基础设置
# =========================

st.set_page_config(
    page_title="BMI Health Mirror",
    page_icon="🪞",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# =========================
# 2. 全局视觉样式
# =========================

st.markdown(
"""
<style>

/* =========================
   整体页面
========================= */

.stApp {
    background:
        radial-gradient(
            circle at top right,
            rgba(214, 220, 255, 0.28),
            transparent 28%
        ),
        linear-gradient(
            180deg,
            #fffdf8 0%,
            #faf9f6 100%
        );

    color: #55506f;
}


.block-container {
    max-width: 1180px;
    padding-top: 2.2rem;
    padding-bottom: 4rem;
}


[data-testid="stHeader"] {
    background: transparent;
}


/* =========================
   Hero
========================= */

.hero {
    position: relative;
    overflow: hidden;

    padding: 2.8rem 3rem;
    margin-bottom: 2rem;

    background: rgba(255, 255, 255, 0.70);

    border:
        1px solid rgba(173, 177, 220, 0.28);

    border-radius: 28px;

    box-shadow:
        0 18px 50px rgba(112, 113, 155, 0.08);

    backdrop-filter: blur(12px);
}


.hero::before {
    content: "";

    position: absolute;

    width: 240px;
    height: 240px;

    right: -50px;
    top: -80px;

    border-radius: 50%;

    background:
        radial-gradient(
            circle,
            rgba(191, 201, 255, 0.28),
            rgba(191, 201, 255, 0)
        );

    pointer-events: none;
}


.hero-tag {
    display: inline-block;

    padding: 0.38rem 0.8rem;
    margin-bottom: 1rem;

    border-radius: 999px;

    background: rgba(225, 228, 255, 0.65);

    color: #8483b8;

    font-size: 0.78rem;
    font-weight: 700;

    letter-spacing: 0.12em;
}


.hero-title {
    margin: 0;

    color: #5f5b82;

    font-size: clamp(2.4rem, 5vw, 4.6rem);
    font-weight: 800;

    letter-spacing: -0.04em;
    line-height: 1;
}


.hero-cn {
    margin-top: 1.3rem;

    color: #565271;

    font-size: 1.45rem;
    font-weight: 800;
}


.hero-desc {
    margin-top: 0.65rem;
    margin-bottom: 0;

    max-width: 760px;

    color: #9490aa;

    font-size: 1rem;

    line-height: 1.8;
}


/* =========================
   小标题
========================= */

.section-kicker {
    margin-bottom: 0.4rem;

    color: #aaa7c9;

    font-size: 0.76rem;
    font-weight: 800;

    letter-spacing: 0.15em;
}


/* =========================
   输入卡片
   与 Hero 同视觉
========================= */

.st-key-health_input_card {
    position: relative;

    background: rgba(255, 255, 255, 0.70) !important;

    border:
        1px solid rgba(173, 177, 220, 0.28) !important;

    border-radius: 28px !important;

    box-shadow:
        0 18px 50px rgba(112, 113, 155, 0.08) !important;

    padding: 2rem 2.4rem !important;

    overflow: hidden;

    backdrop-filter: blur(12px);
}


/* 去掉 Streamlit container 默认边框 */
.st-key-health_input_card
[data-testid="stVerticalBlockBorderWrapper"] {
    background: transparent !important;

    border: none !important;

    box-shadow: none !important;

    padding: 0 !important;
}


/* 输入卡片右上角光晕 */
.st-key-health_input_card::before {
    content: "";

    position: absolute;

    width: 240px;
    height: 240px;

    right: -50px;
    top: -80px;

    border-radius: 50%;

    background:
        radial-gradient(
            circle,
            rgba(191, 201, 255, 0.22),
            rgba(191, 201, 255, 0)
        );

    pointer-events: none;
}


/* =========================
   输入框
========================= */

div[data-baseweb="input"] {
    border-radius: 14px;
}


/* =========================
   Calculate BMI 按钮
========================= */

.stButton > button {
    width: 100%;

    margin-top: 0.8rem;

    padding: 0.82rem 1rem;

    border: none;

    border-radius: 18px;

    background:
        linear-gradient(
            90deg,
            #b5c9c2 0%,
            #aebbd8 100%
        );

    color: white;

    font-size: 1rem;
    font-weight: 700;

    box-shadow:
        0 10px 24px rgba(118, 120, 166, 0.15);

    transition: all 0.2s ease;
}


.stButton > button:hover {
    transform: translateY(-1px);

    background:
        linear-gradient(
            90deg,
            #a9beb7 0%,
            #a3afd1 100%
        );

    color: white;

    box-shadow:
        0 12px 28px rgba(118, 120, 166, 0.18);
}


.stButton > button:focus,
.stButton > button:focus-visible,
.stButton > button:active {
    outline: none !important;
    border: none !important;

    box-shadow:
        0 10px 24px rgba(118, 120, 166, 0.15) !important;
}


/* =========================
   Expander
========================= */

[data-testid="stExpander"] {
    background: rgba(255,255,255,0.72);

    border:
        1px solid rgba(177,181,220,0.25);

    border-radius: 20px;

    overflow: hidden;
}


/* =========================
   Responsive layout helpers
========================= */

.result-card {
    margin-top: 2.5rem;
    padding: 2.2rem 2.4rem;
    background: rgba(255, 255, 255, 0.70);
    border: 1px solid rgba(173, 177, 220, 0.28);
    border-radius: 28px;
    box-shadow: 0 18px 50px rgba(112, 113, 155, 0.08);
}

.result-value {
    font-size: clamp(3.4rem, 10vw, 4.8rem);
}

.range-card {
    margin-top: 1.3rem;
    padding: 1.7rem 2rem;
    background: rgba(255, 255, 255, 0.70);
    border: 1px solid rgba(173, 177, 220, 0.28);
    border-radius: 28px;
    box-shadow: 0 18px 50px rgba(112, 113, 155, 0.06);
}

.range-labels {
    display: grid;
    grid-template-columns: 21.4% 26.2% 19% 33.4%;
    margin-top: 0.8rem;
    color: #8f8a9f;
    font-size: 0.77rem;
    text-align: center;
}

.feedback-card {
    padding: 2rem;
    border: 1px solid rgba(177, 181, 220, 0.24);
    border-radius: 26px;
    box-shadow: 0 12px 34px rgba(107, 108, 150, 0.05);
}

.feedback-spacer {
    height: 35px;
}

.cards-grid {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 1.2rem;
    width: 100%;
}

.metric-card {
    min-width: 0;
    min-height: 205px;
    padding: 1.7rem;
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    background: rgba(255, 255, 255, 0.78);
    border: 1px solid rgba(177, 181, 220, 0.28);
    border-radius: 24px;
    box-shadow: 0 10px 28px rgba(107, 108, 150, 0.05);
}

.metric-value {
    overflow-wrap: anywhere;
}

@media (max-width: 768px) {
    .block-container {
        width: 100%;
        padding: 1rem 1rem 2.5rem;
    }

    .hero {
        padding: 1.7rem 1.25rem;
        margin-bottom: 1rem;
        border-radius: 20px;
    }

    .hero::before,
    .st-key-health_input_card::before {
        width: 170px;
        height: 170px;
        right: -65px;
        top: -65px;
    }

    .hero-tag {
        margin-bottom: 0.75rem;
        font-size: 0.68rem;
        letter-spacing: 0.09em;
    }

    .hero-title {
        font-size: clamp(2rem, 12vw, 3.1rem);
        line-height: 1.05;
        overflow-wrap: anywhere;
    }

    .hero-cn {
        margin-top: 1rem;
        font-size: 1.2rem;
    }

    .hero-desc {
        font-size: 0.94rem;
        line-height: 1.65;
    }

    .st-key-health_input_card {
        padding: 1.4rem 1.15rem !important;
        border-radius: 20px !important;
    }

    /* Streamlit columns are kept side-by-side by default on some versions. */
    [data-testid="stHorizontalBlock"] {
        flex-direction: column;
        gap: 0.35rem !important;
    }

    [data-testid="stHorizontalBlock"] > [data-testid="stColumn"] {
        width: 100% !important;
        flex: 1 1 100% !important;
        min-width: 0 !important;
    }

    /* 16px prevents iOS browsers from zooming when a field receives focus. */
    input,
    button,
    textarea,
    select {
        font-size: 16px !important;
    }

    .stButton > button {
        min-height: 48px;
        margin-top: 0.55rem;
        border-radius: 15px;
    }

    .result-card,
    .range-card {
        margin-top: 1rem;
        padding: 1.35rem 1.15rem;
        border-radius: 20px;
    }

    .range-card {
        overflow-x: hidden;
    }

    .range-labels {
        font-size: 0.64rem;
        line-height: 1.25;
    }

    .range-labels span {
        font-size: 0.61rem !important;
    }

    .feedback-spacer {
        display: none;
    }

    .feedback-card {
        padding: 1.35rem 1.15rem;
        border-radius: 20px;
    }

    .cards-grid {
        grid-template-columns: 1fr;
        gap: 0.85rem;
    }

    .metric-card {
        min-height: 165px;
        padding: 1.35rem 1.2rem;
        border-radius: 20px;
    }

    [data-testid="stImage"] img {
        display: block;
        max-height: 360px;
        object-fit: contain;
    }

    [data-testid="stExpander"] {
        border-radius: 16px;
    }
}

@media (max-width: 390px) {
    .block-container {
        padding-right: 0.75rem;
        padding-left: 0.75rem;
    }

    .hero,
    .st-key-health_input_card {
        border-radius: 18px !important;
    }

    .hero-title {
        font-size: 2rem;
    }

    .range-labels {
        font-size: 0.58rem;
    }
}

</style>
""",
unsafe_allow_html=True
)


# =========================
# 3. Hero
# =========================

st.markdown(
"""
<div class="hero">

<div class="hero-tag">
PERSONAL HEALTH SNAPSHOT
</div>

<h1 class="hero-title">
BMI HEALTH MIRROR
</h1>

<div class="hero-cn">
你的身体状态，一眼看懂
</div>

<p class="hero-desc">
输入身高和体重，快速获得 BMI 分析、
健康体重参考区间以及更贴近你当前状态的生活建议。
</p>

</div>
""",
unsafe_allow_html=True
)


# =========================
# 4. 输入卡片
# =========================

with st.container(
    border=True,
    key="health_input_card"
):

    st.markdown(
"""
<div class="section-kicker">
YOUR HEALTH SNAPSHOT
</div>

<div style="
    color:#625f87;
    font-size:2rem;
    font-weight:800;
    margin-top:0.35rem;
    margin-bottom:0.7rem;
">
填写你的基础信息
</div>

<div style="
    color:#9692aa;
    font-size:1rem;
    line-height:1.7;
    margin-bottom:1.3rem;
">
输入你的身高和体重，即可获得 BMI 分析与健康状态参考。
</div>
""",
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(
        2,
        gap="large"
    )

    with col1:

        height = st.number_input(
            "身高 / Height (cm)",
            min_value=100.0,
            max_value=230.0,
            value=170.0,
            step=0.5
        )


    with col2:

        weight = st.number_input(
            "体重 / Weight (kg)",
            min_value=25.0,
            max_value=250.0,
            value=60.0,
            step=0.5
        )


    calculate = st.button(
        "Calculate BMI｜查看我的 BMI",
        use_container_width=True
    )


# =========================
# 5. BMI 计算
# =========================

if calculate:

    # 身高 cm → m
    height_m = height / 100

    # BMI
    bmi = weight / (height_m ** 2)

    # 正常 BMI 对应的体重范围
    healthy_min = 18.5 * (height_m ** 2)
    healthy_max = 23.9 * (height_m ** 2)


    # =========================
    # 6. BMI 状态判断
    # =========================

    if bmi < 18.5:

        status = "偏瘦"
        status_en = "Underweight"

        status_text = (
            "当前体重偏轻。建议规律三餐，增加优质蛋白和主食摄入，"
            "不要为了“瘦”而长期吃得过少。"
        )

        distance = healthy_min - weight


    elif bmi < 24:

        status = "正常"
        status_en = "Normal"

        status_text = (
            "你的 BMI 目前处于正常范围。继续保持均衡饮食、"
            "规律运动和稳定睡眠即可，不需要为了数字刻意减重。"
        )

        distance = 0


    elif bmi < 28:

        status = "超重"
        status_en = "Overweight"

        status_text = (
            "当前 BMI 偏高，可以从每天 20–30 分钟快走、慢跑或骑车开始，"
            "同时适当减少高油、高糖食物的摄入频率。"
        )

        distance = weight - healthy_max


    else:

        status = "肥胖"
        status_en = "Obesity"

        status_text = (
            "当前 BMI 已进入较高区间。BMI 只是健康筛查指标，"
            "建议结合腰围、血压、血脂等信息综合判断，"
            "并在需要时咨询医生或营养专业人士。"
        )

        distance = weight - healthy_max


    # =========================
    # 7. 状态颜色
    # =========================

    bmi_display = round(bmi, 2)

    if status == "偏瘦":

        status_color = "#E7B86A"
        status_bg = "#FFF7E8"

    elif status == "正常":

        status_color = "#78A99B"
        status_bg = "#EFF8F4"

    elif status == "超重":

        status_color = "#E38D72"
        status_bg = "#FFF2ED"

    else:

        status_color = "#C97972"
        status_bg = "#FFF0EF"


       # =========================
    # 8. BMI 主结果卡
    # =========================

    result_html = f"""
<div style="margin-top:2.5rem;padding:2.2rem 2.4rem;background:rgba(255,255,255,0.70);border:1px solid rgba(173,177,220,0.28);border-radius:28px;box-shadow:0 18px 50px rgba(112,113,155,0.08);">

<div style="color:#aaa7c9;font-size:0.76rem;font-weight:800;letter-spacing:0.14em;margin-bottom:0.9rem;">
YOUR BMI RESULT
</div>

<div style="font-size:4.8rem;font-weight:800;color:{status_color};line-height:1;letter-spacing:-0.05em;">
{bmi_display}
</div>

<div style="margin-top:0.7rem;font-size:1.25rem;font-weight:800;color:#5b5874;">
{status_en} ｜ {status}
</div>

<div style="margin-top:1.1rem;color:#8a86a0;font-size:1rem;line-height:1.9;max-width:760px;">
{status_text}
</div>

</div>
"""


    # =========================
    # 9. BMI 区间条
    # =========================

    bmi_min_scale = 14
    bmi_max_scale = 35

    bmi_for_pointer = min(
        max(bmi, bmi_min_scale),
        bmi_max_scale
    )

    pointer_percent = (
        (bmi_for_pointer - bmi_min_scale)
        /
        (bmi_max_scale - bmi_min_scale)
        * 100
    )


    range_html = f"""
<div style="margin-top:1.3rem;padding:1.7rem 2rem;background:rgba(255,255,255,0.70);border:1px solid rgba(173,177,220,0.28);border-radius:28px;box-shadow:0 18px 50px rgba(112,113,155,0.06);">

<div style="margin-bottom:1.2rem;color:#696580;font-size:1rem;font-weight:700;">
BMI Range｜BMI 区间
</div>

<div style="position:relative;padding-top:34px;padding-bottom:8px;">

<div style="position:absolute;left:{pointer_percent}%;top:0;transform:translateX(-50%);text-align:center;">

<div style="display:inline-block;padding:4px 9px;background:#5e5a78;color:white;border-radius:999px;font-size:0.72rem;font-weight:700;">
{bmi_display}
</div>

<div style="width:0;height:0;margin:auto;border-left:5px solid transparent;border-right:5px solid transparent;border-top:7px solid #5e5a78;">
</div>

</div>


<div style="display:flex;height:16px;overflow:hidden;border-radius:999px;">

<div style="width:21.4%;background:#F2CF8C;"></div>

<div style="width:26.2%;background:#9CC9BA;"></div>

<div style="width:19%;background:#E7A07E;"></div>

<div style="width:33.4%;background:#C97D78;"></div>

</div>


<div style="display:grid;grid-template-columns:21.4% 26.2% 19% 33.4%;margin-top:0.8rem;font-size:0.77rem;color:#8f8a9f;text-align:center;">

<div>
偏瘦<br>
<span style="font-size:0.70rem;">&lt;18.5</span>
</div>

<div>
正常<br>
<span style="font-size:0.70rem;">18.5–23.9</span>
</div>

<div>
超重<br>
<span style="font-size:0.70rem;">24–27.9</span>
</div>

<div>
肥胖<br>
<span style="font-size:0.70rem;">≥28</span>
</div>

</div>

</div>

</div>
"""

    st.markdown(
        range_html,
        unsafe_allow_html=True
    )


    # =========================
    # 10. 像素人物 + 健康反馈
    # =========================

    if status == "偏瘦":

        character_path = ASSETS_DIR / "underweight.png"

        feedback_title = "今天也要好好吃饭！"

        feedback_text = (
            "当前体重偏轻。建议规律三餐，增加主食、蛋白质和健康脂肪的摄入，"
            "不要为了追求更低体重而长期吃得过少。"
        )

        feedback_bg = "#FFF8EC"
        feedback_accent = "#E8B86A"


    elif status == "正常":

        character_path = ASSETS_DIR / "normal.png"

        feedback_title = "状态不错，继续保持！"

        feedback_text = (
            "你的 BMI 处于正常范围。继续保持均衡饮食、规律运动和稳定睡眠，"
            "不需要为了数字刻意减重。"
        )

        feedback_bg = "#F2F8F4"
        feedback_accent = "#82AA9B"


    elif status == "超重":

        character_path = ASSETS_DIR / "overweight.png"

        feedback_title = "动起来，但不用着急！"

        feedback_text = (
            "当前 BMI 偏高。可以从每天增加 20–30 分钟快走、慢跑或骑行开始，"
            "同时减少高油、高糖食品和含糖饮料的摄入频率。"
        )

        feedback_bg = "#FFF3EE"
        feedback_accent = "#E28F74"


    else:

        character_path = "assets/obesity.png"

        feedback_title = "多关注一步，更安心一点！"

        feedback_text = (
            "当前 BMI 已进入较高区间。BMI 只是筛查指标，建议同时关注腰围、"
            "血压、血脂和血糖等信息；如有基础疾病或身体不适，"
            "可咨询医生或营养专业人士。"
        )

        feedback_bg = "#F4F8F0"
        feedback_accent = "#8DAA87"


    st.markdown(
        '<div style="height:1.5rem;"></div>',
        unsafe_allow_html=True
    )


    character_col, advice_col = st.columns(
        [0.9, 1.35],
        gap="large",
        vertical_alignment="top"
    )


    with character_col:

        st.image(
            character_path,
            use_container_width=True
        )


    with advice_col:

        st.markdown(
            '<div style="height:35px;"></div>',
            unsafe_allow_html=True
        )

        feedback_html = f"""
<div style="padding:2rem;background:{feedback_bg};border:1px solid rgba(177,181,220,0.24);border-radius:26px;box-shadow:0 12px 34px rgba(107,108,150,0.05);">

<div style="color:#aaa7c9;font-size:0.74rem;font-weight:800;letter-spacing:0.14em;margin-bottom:0.8rem;">
PERSONAL FEEDBACK
</div>

<div style="font-size:1.65rem;font-weight:800;color:{feedback_accent};margin-bottom:1rem;">
{feedback_title}
</div>

<div style="color:#716d82;font-size:1rem;line-height:1.9;">
{feedback_text}
</div>

</div>
"""

        st.markdown(
            feedback_html,
            unsafe_allow_html=True
        )


    # =========================
    # 11. 三张详细指标卡
    # =========================

    if status == "偏瘦":

        distance_text = f"+{distance:.1f} kg"
        distance_note = "距正常范围下限"

    elif status == "正常":

        distance_text = "已在范围内"
        distance_note = "当前体重状态"

    else:

        distance_text = f"-{distance:.1f} kg"
        distance_note = "距正常范围上限"


    healthy_range_text = (
        f"{healthy_min:.1f} ~ {healthy_max:.1f} kg"
    )


    st.markdown(
        '<div style="height:1.8rem;"></div>',
        unsafe_allow_html=True
    )


    st.markdown(
"""
<div style="color:#aaa7c9;font-size:0.76rem;font-weight:800;letter-spacing:0.14em;margin-bottom:0.45rem;">
HEALTH SNAPSHOT
</div>

<div style="color:#625f87;font-size:1.65rem;font-weight:800;margin-bottom:1.15rem;">
你的详细 BMI 分析
</div>
""",
        unsafe_allow_html=True
    )


    cards_html = f"""
<div style="display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:1.2rem;width:100%;">

<div style="height:205px;padding:1.7rem;background:rgba(255,255,255,0.78);border:1px solid rgba(177,181,220,0.28);border-radius:24px;box-shadow:0 10px 28px rgba(107,108,150,0.05);box-sizing:border-box;display:flex;flex-direction:column;">

<div style="height:34px;color:#aaa7c9;font-size:0.72rem;font-weight:800;letter-spacing:0.12em;">
YOUR BMI
</div>

<div style="height:90px;display:flex;align-items:center;color:#7774ad;font-size:2.7rem;font-weight:800;">
{bmi_display}
</div>

<div style="margin-top:auto;color:#77738b;font-size:0.92rem;">
当前分类：{status}
</div>

</div>


<div style="height:205px;padding:1.7rem;background:rgba(255,255,255,0.78);border:1px solid rgba(177,181,220,0.28);border-radius:24px;box-shadow:0 10px 28px rgba(107,108,150,0.05);box-sizing:border-box;display:flex;flex-direction:column;">

<div style="height:34px;color:#aaa7c9;font-size:0.72rem;font-weight:800;letter-spacing:0.12em;">
HEALTHY WEIGHT RANGE
</div>

<div style="height:90px;display:flex;align-items:center;color:#7774ad;font-size:1.8rem;font-weight:800;">
{healthy_range_text}
</div>

<div style="margin-top:auto;color:#77738b;font-size:0.92rem;">
根据你的身高估算
</div>

</div>


<div style="height:205px;padding:1.7rem;background:rgba(255,255,255,0.78);border:1px solid rgba(177,181,220,0.28);border-radius:24px;box-shadow:0 10px 28px rgba(107,108,150,0.05);box-sizing:border-box;display:flex;flex-direction:column;">

<div style="height:34px;color:#aaa7c9;font-size:0.72rem;font-weight:800;letter-spacing:0.12em;">
DISTANCE TO NORMAL
</div>

<div style="height:90px;display:flex;align-items:center;color:#7774ad;font-size:1.8rem;font-weight:800;">
{distance_text}
</div>

<div style="margin-top:auto;color:#77738b;font-size:0.92rem;">
{distance_note}
</div>

</div>

</div>
"""

    st.markdown(
        cards_html,
        unsafe_allow_html=True
    )


    # =========================
    # 12. BMI 小知识
    # =========================

    st.markdown(
        '<div style="height:1.8rem;"></div>',
        unsafe_allow_html=True
    )


    with st.expander(
        "What BMI can and cannot tell you｜BMI 能告诉你什么？"
    ):

        st.markdown(
"""
BMI 是一种根据 **身高和体重** 计算出的身体质量指数，
可以用于快速判断一个人的体重是否大致处于合理范围。

但 BMI 也有明显局限：

- 它不能直接测量体脂率
- 它不能区分肌肉和脂肪
- 它不能反映脂肪具体分布位置
- 对运动员、健身人群等特殊群体，BMI 可能并不能完全代表真实健康状态

所以 BMI 更适合作为一种 **初步筛查指标**，
而不是完整的健康诊断结果。
"""
        )


    # =========================
    # 13. 健康提示
    # =========================

    st.markdown(
"""
<div style="margin-top:1.2rem;padding:1.25rem 1.5rem;background:rgba(237,238,250,0.55);border:1px solid rgba(177,181,220,0.24);border-radius:20px;color:#77738b;font-size:0.9rem;line-height:1.8;">

<strong style="color:#6f6b90;">
Health Note｜健康提示
</strong>

<br>

BMI 仅用于体重状态的基础筛查，不能替代专业医学诊断。
如存在明显身体不适、基础疾病或特殊健康情况，
建议咨询医生或相关专业人士。

</div>
""",
        unsafe_allow_html=True
    )
