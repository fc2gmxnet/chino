import streamlit as st
import pandas as pd
import random

# --- Data setup ---
df_dictionary = {'Lesson': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 'Column1': ['听说你男朋友李进跟你是一个学校的，是你同学吗？', '他学的是新闻，我学的是法律，我和他不是一个班。', '那你们俩是怎么认识的？', '我们是在一次足球比赛中认识的。', '他一个人踢进两个球，我对他印象很深。', '后来就慢慢熟悉了。', '他不仅足球踢得好，性格也不错。', '李老师，我下个月5号就要结婚了。', '你们不是才认识一个月？', '虽然我们认识的时间不长，但我从来没这么快乐过。', '两个人在一起，最好能有共同的兴趣和爱好。', '我们有很多共同的爱好，经常一起打球、唱歌、做菜。', '看来你真的找到适合你的人了。', '祝你们幸福！', '听说您跟妻子结婚快二十年了？', '到6月9号，我们就结婚二十年了。', '这么多年，我们的生活一直挺幸福的。', '我和丈夫刚结婚的时候，每天都觉得很新鲜。', '两个人共同生活，只有浪漫和新鲜感是不够的。', '您说的对！我现在每天看到的都是他的缺点。', '两个人在一起时间长了，就会有很多问题。', '只有接受了他的缺点，你们才能更好地一起生活。', '很多女孩子羡慕浪漫的爱情。', '那什么是浪漫呢？', '中年人说：浪漫是即使晚上加班到零点，到家时，自己家里也还亮着灯。', '老年人说：浪漫其实就像歌中唱的那样，“我能想到最浪漫的事，就是和你一起慢慢变老。”', '其实，让我们感动的，就是生活中简单的爱情。', '有时候，简单就是最大的幸福。'], 'Column3': ['I heard your boyfriend Li Jin is from the same school as you. Is he your classmate?', 'He studies journalism, I study law. We’re not in the same class.', 'So how did you two meet?', 'We met during a soccer match.', 'He scored two goals by himself. I had a deep impression of him.', 'Later, we gradually got to know each other.', 'Not only does he play soccer well, but he also has a good personality.', 'Teacher Li, I’m getting married on the 5th of next month.', 'Haven’t you only known each other for a month?', 'Although we haven’t known each other long, I’ve never been this happy.', 'When two people are together, it’s best to have common interests and hobbies.', 'We have many shared hobbies: we often play ball, sing, and cook together.', 'It seems you’ve truly found someone suitable for you.', 'Wishing you both happiness!', 'I heard you and your wife have been married for almost 20 years?', 'By June 9th, we’ll have been married for 20 years.', 'All these years, our life has been quite happy.', 'When my husband and I just got married, every day felt very fresh.', 'For two people living together, romance and freshness alone are not enough.', 'You’re right! Now all I see every day are his shortcomings.', 'When two people are together for a long time, many problems arise.', 'Only by accepting his flaws can you live better together.', 'Many girls envy romantic love.', 'So what is romance?', 'Middle-aged people say: Romance is even if you work overtime until midnight, the lights are still on when you get home.', 'Elderly people say: Romance is actually like the song says, “The most romantic thing I can think of is growing old with you.”', 'Actually, what moves us is the simple love in everyday life.', 'Sometimes, simplicity is the greatest happiness.'], 'Column2': ['Tīngshuō nǐ nánpéngyou Lǐ Jìn gēn nǐ shì yī gè xuéxiào de, shì nǐ tóngxué ma?', 'Tā xué de shì xīnwén, wǒ xué de shì fǎlǜ, wǒ hé tā bù shì yī gè bān.', 'Nà nǐmen liǎ shì zěnme rènshi de?', 'Wǒmen shì zài yī cì zúqiú bǐsài zhōng rènshi de.', 'Tā yī gè rén tī jìn liǎng gè qiú, wǒ duì tā yìnxiàng hěn shēn.', 'Hòulái jiù mànmàn shúxī le.', 'Tā bùjǐn zúqiú tī de hǎo, xìnggé yě búcuò.', 'Lǐ lǎoshī, wǒ xià gè yuè wǔ hào jiù yào jiéhūn le.', 'Nǐmen bù shì cái rènshi yī gè yuè?', 'Suīrán wǒmen rènshi de shíjiān bù cháng, dàn wǒ cónglái méi zhème kuàilè guò.', 'Liǎng gè rén zài yīqǐ, zuì hǎo néng yǒu gòngtóng de xìngqù hé àihào.', 'Wǒmen yǒu hěn duō gòngtóng de àihào, jīngcháng yīqǐ dǎqiú, chànggē, zuò cài.', 'Kànlái nǐ zhēn de zhǎodào shìhé nǐ de rén le.', 'Zhù nǐmen xìngfú!', 'Tīngshuō nín gēn qīzi jiéhūn kuài èrshí nián le?', 'Dào liù yuè jiǔ hào, wǒmen jiù jiéhūn èrshí nián le.', 'Zhème duō nián, wǒmen de shēnghuó yīzhí tǐng xìngfú de.', 'Wǒ hé zhàngfu gāng jiéhūn de shíhòu, měitiān dōu juéde hěn xīnxiān.', 'Liǎng gè rén gòngtóng shēnghuó, zhǐyǒu làngmàn hé xīnxiān gǎn shì bùgòu de.', 'Nín shuō de duì! Wǒ xiànzài měitiān kàndào de dōu shì tā de quēdiǎn.', 'Liǎng gè rén zài yīqǐ shíjiān cháng le, jiù huì yǒu hěn duō wèntí.', 'Zhǐyǒu jiēshòu le tā de quēdiǎn, nǐmen cái néng gèng hǎo de yīqǐ shēnghuó.', 'Hěn duō nǚ háizi xiànmù làngmàn de àiqíng.', 'Nà shénme shì làngmàn ne?', 'Zhōngnián rén shuō: Làngmàn shì jíshǐ wǎnshàng jiābān dào língdiǎn, dàojiā shí, zìjǐ jiālǐ yě hái liàngzhe dēng.', 'Lǎonián rén shuō: Làngmàn qíshí jiù xiàng gē zhōng chàng de nàyàng, “Wǒ néng xiǎngdào zuì làngmàn de shì, jiùshì hé nǐ yīqǐ mànmàn biànlǎo.”', 'Qíshí, ràng wǒmen gǎndòng de, jiùshì shēnghuó zhōng jiǎndān de àiqíng.', 'Yǒu shíhou, jiǎndān jiùshì zuì dà de xìngfú.']}
df = pd.DataFrame(df_dictionary)
df['Lesson'] = df['Lesson'].astype(str)  # Ensure lessons are strings

# --- Page configuration ---
st.set_page_config(
    page_title='maps - Pesquisa Google',
    page_icon='https://github.com/fc2gmxnet/chino/raw/main/icons8-google-logo-48.png',
    layout='wide'
)

# --- UI: Toggle and Dropdown side by side ---
col1, col2 = st.columns([2, 1])
with col1:
    toggle = st.toggle("HSK 4:    用中文回答")
with col2:
    selected_lesson = st.selectbox("Lesson", sorted(df['Lesson'].unique()))

# --- Language columns ---
if toggle:
    columna_pregunta = 2
    columna_respuesta = 1
else:
    columna_pregunta = 1
    columna_respuesta = 2

# --- Filter by selected lesson ---
filtered_df = df[df['Lesson'] == selected_lesson]

# --- Session state for random index ---
if "random_index" not in st.session_state or st.session_state.get("last_lesson") != selected_lesson:
    st.session_state.random_index = random.randint(0, len(filtered_df) - 1) if not filtered_df.empty else None
    st.session_state.last_lesson = selected_lesson

# --- Function to pick a new random row ---
def get_new_random_row():
    if not filtered_df.empty:
        st.session_state.random_index = random.randint(0, len(filtered_df) - 1)

# --- Display question ---
if st.session_state.random_index is not None:
    random_row = filtered_df.iloc[st.session_state.random_index]
    st.subheader(random_row.iloc[columna_pregunta])

    # Reveal answer
    if st.button('???'):
        st.subheader(random_row.iloc[3])
        if columna_respuesta == 1:
            st.title(random_row.iloc[columna_respuesta])
        else:
            st.subheader(random_row.iloc[columna_respuesta])

    # Next question
    if st.button("+++"):
        get_new_random_row()
        st.rerun()
else:
    st.warning("No questions available for this lesson.")
