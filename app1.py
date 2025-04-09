import streamlit as st                      # Para crear apps en HTML
from streamlit-keyboard import keypress     # Para crear shortcuts en botones
import pandas as pd                         # Para trabajar con dataframes (tablas)
import random                               # Para trabajar con aleatoriedades

df = pd.DataFrame({
    'Column1': ['爷爷常常让我给他读报纸',
 '这个消息是我从报纸上看到的',
 '考试的时候不可以使用铅笔',
 '妈妈给我买了一块新手表',
 '她用手机给我拍了一些照片',
 '开会的时候，请大家关闭手机',
 '这个公园不需要门票',
 '他去火车站买火车票了',
 '请帮我开一下门',
 '有人在外面敲门',
 '生病了就应该吃药',
 '这个药一天吃三次',
 '我们可以坐公共汽车去图书馆',
 '他是公共汽车司机 (公交车）',
 '这条路不好走',
 '请在路边停一下',
 '为了健康，别喝太多咖啡',
 '我要去超市买牛奶',
 '冰箱里还有牛奶吗？',
 '这个超市的西瓜又好吃又便宜',
 '十块钱能买几个鸡蛋？',
 '北方人喜欢吃面条',
 '南方人喜欢吃米饭',
 '妈妈给我煮了一碗面条',
 '你吃过羊肉火锅吗？',
 '我不在家的时候，你要好好照顾这些鱼',
 '我老婆有一双漂亮的棕眼睛',
 '闭上眼睛，休息一会儿吧',
 '你最近身体怎么样？',
 '今年冬天会下雪吗？',
 '奶奶的头发像雪一样白',
 '这次考试很简单',
 '你一定能通过明天的考试',
 '我们每天早上八点上课',
 '我很喜欢上汉语课',
 '这道数学题怎么做？',
 '这次考试一共有四道题',
 '请你回答我的问题',
 '我的手机有一点问题',
 '医生告诉我要多做运动',
 '游泳是很好的健身运动',
 '她的眼睛是什么颜色的？',
 '这件衣服有几种颜色？',
 '他病了好长时间',
 '没时间了，你快一点儿',
 '孔子学院旁边有一个公园',
 '我想坐在窗户旁边',
 '一直往前走，图书馆就在你的右边',
 '过马路的时候，先看左边，再看右边',
 '右边的电梯坏了，我们坐左边的吧',
 '你往左边站一点儿',
 '门外停了一辆新车',
 '王经理现在在国外',
 '我们每天要工作八个小时',
 '你已经迟到一个小时了',
 '这件衬衫是我去年买的',
 '我去年就已经毕业了',
 '你今天早上吃了什么？',
 '她习惯在早上锻炼身体',
 '晚上九点以后不要给我打电话',
 '星期一到星期五是工作日',
 '圣诞节是每年的12月25日 (/ 号)',
 '我刚过完33岁的生日',
 '妈妈的生日和爸爸的生日是同一天',
 '我长得像爸爸，弟弟长得像妈妈',
 '我真希望我有一辆新车',
 '我和姐姐在同一个学校学习',
 '我妹妹最近在减肥',
 '姐姐比妹妹高一点儿',
 '妈妈让我照顾弟弟和妹妹',
 '我爱我妻子',
 '我很饿因为我今天早上不吃早餐',
 '她决定和她的丈夫离婚',
 '丈夫比妻子大四岁',
 '他们结婚十年了，一直没有孩子',
 '孩子们都很喜欢吃糖',
 '这家饭店的服务员很热情',
 '服务员，拿两瓶啤酒',
 '我有很多事情要做',
 '这件事情没有这么简单',
 '这个词是什么意思？',
 '我明白你的意思了',
 '请问一下，这家宾馆怎么走？',
 '她住在公司附近的宾馆里',
 '我请假了，明天不去公司',
 '他去火车站接他的女朋友了',
 '从这儿去机场要一个小时',
 '机场的东西一般都很贵',
 '这家宾馆一共有六十九个房间',
 '我终于有自己的房间了',
 '我们的教室在三楼',
 '孩子们在教室里认真地学习',
 '今天太冷了，我不想出门',
 '我在家等妈妈回来做饭',
 '你准备送她什么生日礼物？',
 '这道题我也不会，你去问老师吧',
 '你吃完饭记得洗碗',
 '爸爸笑着给我们讲他年轻时候的故事',
 '你找到新的工作了吗？',
 '我还找新的工作',
 '你走快一点儿，我们要迟到了',
 '如果你到了，你就先点菜吧',
 '别人都懂了，只有你还不明白',
 '请问您姓什么？',
 '我家离学校很近',
 '我终于把这本书看完了',
 '你们今天想去哪儿玩儿？',
 '现在我们开始学习吧',
 '我决定从明天开始学习做饭',
 '天气太冷了，我一点儿都不想起床',
 '很多中老年人喜欢在晚饭后去广场上跳舞',
 '我最近很忙，都没有时间去旅游',
 '他每天骑自行车去上班',
 '医生说他需要休息',
 '你别一直坐着，站起来运动一下',
 '他每天起床后，都会去公园跑步',
 '我最近在学游泳',
 '我听说你生病了，现在好一点儿了吗？',
 '上课的时候不要说话',
 '她打电话告诉我，她会晚一点儿到',
 '老师正在给我们介绍新同学',
 '你准备什么时候回国？',
 '我觉得这个电影一点儿都不好看',
 '我希望爸爸妈妈身体健康',
 '今天可能会下雨',
 '哥哥说明天教我打篮球',
 '操场上有很多孩子在踢足球',
 '他的牙齿非常白',
 '外面太黑了，我什么都看不见',
 '我的黑头发越来越少，白头发越来越多',
 '你的脸怎么这么红？',
 '我们的新邻居是外国人',
 '这个城市哪儿都好，就是房子太贵了',
 '你为什么买这么贵的手机？',
 '他在这儿等了你很长时间了',
 '这条裤子太长了，有短一点儿的吗？',
 '世界上最高的楼在哪个国家？',
 '人们的生活水平越来越高了',
 '爸爸工作很忙，每天都很晚回家',
 '我换了新工作，比以前更忙了',
 '这个字你写错了，应该这样写',
 '你知道你哪里做错了吗？',
 '我家和他家离得很近',
 '那家饭店太远了，我们找一家近一点儿的吧',
 '这儿离火车站有多远？',
 '离我家不远的地方有一家医院',
 '你快一点儿，火车要开了',
 '老师说得太快了，我没听清楚',
 '外面正在下雨，你开车的时候慢一点儿',
 '我们走得很慢，走了很久才到家',
 '今天是晴天，我们一起出去玩儿吧',
 '今天是阴天，有点儿冷',
 '我们班有一个又高又帅的男同学',
 '我在女厕所门前见到了一个钱包',
 '这个面包太好吃了，我想再吃一个',
 '我打羽毛球打得还可以',
 '这个电影还可以，你可以去看一下',
 '火车票比飞机票更便宜',
 '哪里能买到又好吃又便宜的水果？',
 '和你聊天我觉得很快乐',
 '我要给大家都讲一个故事',
 '这个活动每个人都必须参加',
 '那本书你看完了吗？你什么时候把它还给我？',
 '他们为什么这么高兴？',
 '哥哥正在学习，你别打扰他',
 '你别喝酒，一会儿还要开车呢',
 '这件事你做得非常好',
 '我们认识九年了，我非常了解她',
 '这件衣服还不错',
 '我还想去一次北京',
 '你还在那个公司上班吗？',
 '你能不能再说一遍？',
 '你别再给我打电话了',
 '这套西装还是太小了，有没有再大一点儿的？',
 '你写完作业再看电视',
 '我先想想再回答你',
 '这双鞋子还不错，就买这双吧',
 '楼下有个超市，就去那里买一点儿菜吧',
 '我今天五点钟就起床了',
 '他一十五岁就结婚了',
 '我们已经一年没有见面了',
 '你来晚了，他已经回去了',
 '王经理正在开会',
 '奶奶正在学习用手机上网',
 '这真是一个好办法',
 '读完这本书最少需要一个星期',
 '这是我们班成绩最好的学生',
 '很多人参加了这个活动',
 '她一个星期去看两次电影',
 '保罗已经两个月没来上汉语课了',
 '他这次考试考了一百分',
 '这个公司有几千个人',
 '我花了八块钱买了一把花',
 '你今天第一天去上班，千万别迟到了',
 '我再给你一次机会',
 '我突然想起来一件事情',
 '他刚才拍了我一下',
 '你在这儿等一下，我马上回来',
 '请你帮我拿一下我的包',
 '她唱歌唱得很好听。',
 '你找我有事吗？我正忙着呢',
 '我今年比去年胖了',
 '你是从哪里来的？',
 '你有什么话想对我说吗？',
 '你要对自己有信心',
 '请问飞往北京的飞机起飞了吗？',
 '请问飞往上海的飞机降落了吗？',
 '虽然这条裙子很贵，但她还是买了',
 '虽然工作很忙，但是我一直坚持学习汉语',
 '因为她生病了，所以她今天没来',
 '你还在因为那件事情生气吗？',
 '你还小，所以你不懂'],
    'Column2': ['Yéye chángcháng ràng wǒ gěi tā dú bàozhǐ',
 'zhè ge xiāoxi shì wǒ cóng bàozhǐ shang kàn dào de',
 'kǎoshì de shíhou bù kěyǐ shǐyòng qiānbǐ',
 'māma gěi wǒ mǎi le yī kuài xīn shǒubiǎo',
 'tā yòng shǒujī gěi wǒ pāi le yī xiē zhàopiàn',
 'kāihuì de shíhou, qǐng dàjiā guānbì shǒujī',
 'zhè ge gōngyuán bù xūyào ménpiào',
 'tā qù huǒchē zhàn mǎi huǒchē piào le',
 'qǐng bāng wǒ kāi yī xià mén',
 'yǒu rén zài wàimian qiāo mén',
 'shēng bìng le jiù yīnggāi chī yào',
 'zhè ge yào yī tiān chī sān cì',
 'wǒmen kěyǐ zuò gōnggòngqìchē qù túshūguǎn',
 'tā shì gōnggòngqìchē sījī (gōngjiāochē)',
 'zhè tiáo lù bù hǎo zǒu',
 'qǐng zài lù biān tíng yī xià',
 'wèile jiànkāng, bié hē tài duō kāfēi',
 'wǒ yào qù chāoshì mǎi niúnǎi',
 'bīngxiāng lǐ hái yǒu niúnǎi ma?',
 'Zhè ge chāoshì de xīguā yòu hǎo chī yòu piányi',
 'shí kuài qián néng mǎi jǐ ge jīdàn?',
 'Běifāng rén xǐhuan chī miàntiáo',
 'nánfāng rén xǐhuan chī mǐfàn',
 'māma gěi wǒ zhǔ le yī wǎn miàntiáo',
 'nǐ chī guo yángròu huǒguō ma?',
 'Wǒ bù zài jiā de shíhou, nǐ yào hǎohao zhàogu zhè xiē yú',
 'wǒ lǎopó yǒu yī shuāng piàoliang de zōng yǎnjing',
 'bì shang yǎnjing, xiūxi yī huìr ba',
 'nǐ zuìjìn shēntǐ zěnme yàng?',
 'jīn nián dōngtiān huì xià xuě ma?',
 'Nǎinai de tóufa xiàng xuě yí yàng bái',
 'zhè cì kǎoshì hěn jiǎndān',
 'nǐ yīdìng néng tōngguò míngtiān de kǎoshì',
 'wǒmen měitiān zǎoshang bā diǎn shàng kè',
 'wǒ hěn xǐhuan shàng hànyǔ kè',
 'zhè dào shùxué tí zěnme zuò?',
 'Zhè cì kǎoshì yī gòng yǒu sì dào tí',
 'qǐng nǐ huídá wǒ de wèntí',
 'wǒ de shǒujī yǒu yī diǎn wèntí',
 'yīshēng gàosu wǒ yào duō zuò yùndòng',
 'yóuyǒng shì hěn hǎo de jiànshēn yùndòng',
 'tā de yǎnjing shì shénme yánsè de?',
 'Zhè jiàn yīfu yǒu jǐ zhǒng yánsè?',
 'Tā bìng le hǎo cháng shíjiān',
 'méi shíjiān le, nǐ kuài yīdiǎnr',
 'kǒngzǐ xuéyuàn pángbiān yǒu yī ge gōngyuán',
 'wǒ xiǎng zuò zài chuānghu pángbiān',
 'yī zhí wǎng qián zǒu, túshūguǎn jiù zài nǐ de yòubian',
 'guò mǎlù de shíhou, xiān kàn zuǒbian, zài kàn yòubian',
 'yòubian de diàntī huài le, wǒmen zuò zuǒbian de ba',
 'nǐ wǎng zuǒbian zhàn yī diǎnr',
 'mén wài tíng le yī liàng xīn chē',
 'wáng jīnglǐ xiànzài zài guówài',
 'wǒmen měitiān yào gōngzuò bā ge xiǎoshí',
 'nǐ yǐjīng chí dào yī ge xiǎoshí le',
 'zhè jiàn chènshān shì wǒ qù nián mǎi de',
 'wǒ qù nián jiù yǐjīng bìyè le',
 'nǐ jīntiān zǎoshang chī le shénme?',
 'Tā xíguàn zài zǎoshang duànliàn shēntǐ',
 'wǎnshang jiǔ diǎn yǐhòu bù yào gěi wǒ dǎ diànhuà',
 'xīngqīyī dào xīngqīwǔ shì gōngzuò rì',
 'shèngdàn jié shì měi nián de 12 yuè 25 rì (/ hào) (Birth of Saint = Christmas)',
 'wǒ gāng guò wán 33 suì de shēngrì',
 'māma de shēngrì hé bàba de shēngrì shì tóng yī tiān',
 'wǒ zhǎng de xiàng bàba, dìdi zhǎng de xiàng māma',
 'wǒ zhēn xīwàng wǒ yǒu yī liàng xīn chē',
 'wǒ hé jiějie zài tóng yī ge xuéxiào xuéxí',
 'wǒ mèimei zuìjìn zài jiǎnféi',
 'jiějie bǐ mèimei gāo yī diǎnr',
 'māma ràng wǒ zhàogu dìdi hé mèimei',
 'wǒ ài wǒ qīzi',
 'wǒ hěn è yīnwèi wǒ jīntiān zǎoshang bù chī zǎocān',
 'tā juédìng hé tā de zhàngfu líhūn',
 'zhàngfu bǐ qīzi dà sì suì',
 'tāmen jiéhūn shí nián le, yī zhí méi yǒu háizi',
 'háizimen dōu hěn xǐhuan chī táng',
 'zhè jiā fàndiàn de fúwùyuán hěn rèqíng',
 'fúwùyuán, ná liǎng píng píjiǔ',
 'wǒ yǒu hěn duō shìqing yào zuò',
 'zhè jiàn shìqing méi yǒu zhème jiǎndān (it seemed simple at first)',
 'zhè ge cí shì shénme yìsi?',
 'Wǒ míngbai nǐ de yìsi le',
 'qǐng wèn yī xià, zhè jiā bīnguǎn zěnme zǒu?',
 'Tā zhù zài gōngsī fùjìn de bīnguǎn li',
 'wǒ qǐng jià le, míngtiān bù qù gōngsī',
 'tā qù huǒchē zhàn jiē tā de nǚ péngyou le',
 'cóng zhèr qù jīchǎng yào yī ge xiǎoshí',
 'jīchǎng de dōngxi yī bān dōu hěn guì',
 'zhè jiā bīnguǎn yī gòng yǒu liùshíjiǔ ge fángjiān',
 'wǒ zhōngyú yǒu zìjǐ de fángjiān le',
 'wǒmen de jiàoshì zài sān lóu',
 'háizimen zài jiàoshì li rènzhēn de xuéxí',
 'Jīntiān tài lěng le, wǒ bù xiǎng chū mén',
 'wǒ zài jiā děng māma huí lái zuò fàn',
 'nǐ zhǔnbèi sòng tā shénme shēngrì lǐwù?',
 'Zhè dào tí wǒ yě bù huì, nǐ qù wèn lǎoshī ba',
 'nǐ chī wán fàn jìde xǐ wǎn',
 'bàba xiào zhe gěi wǒmen jiǎng tā niánqīng shíhou de gùshi',
 'nǐ zhǎodào xīn de gōngzuò le ma?',
 'Wǒ hái zhǎo xīn de gōngzuò',
 'nǐ zǒu kuài yī diǎnr, wǒmen yào chí dào le',
 'rúguǒ nǐ dào le, nǐ jiù xiān diǎn cài ba',
 'bié rén dōu dǒng le, zhǐ yǒu nǐ hái bù míngbai',
 'qǐng wèn nín xìng shénme?',
 'Wǒ jiā lí xuéxiào hěn jìn',
 'wǒ zhōngyú bǎ zhè běn shū kàn wán le',
 'nǐmen jīntiān xiǎng qù nǎr wánr?',
 'Xiànzài wǒmen kāishǐ xuéxí ba',
 'wǒ juédìng cóng míngtiān kāishǐ xuéxí zuò fàn',
 'tiānqì tài lěng le, wǒ yī diǎnr dōu bù xiǎng qǐchuáng',
 'Hěn duō zhōng lǎo nián rén xǐhuan zài wǎnfàn hòu qù guǎngchǎng shàng tiàowǔ',
 'wǒ zuìjìn hěn máng, dōu méi yǒu shíjiān qù lǚyóu',
 'tā měitiān qí zìxíngchē qù shàng bān',
 'yīshēng shuō tā xūyào xiūxi',
 'nǐ bié yī zhí zuò zhe, zhàn qǐlái yùndòng yī xià',
 'tā měitiān qǐchuáng hòu, dōu huì qù gōngyuán pǎobù',
 'wǒ zuìjìn zài xué yóuyǒng',
 'wǒ tīng shuō nǐ shēngbìng le, xiànzài hǎo yī diǎnr le ma?',
 'Shàng kè de shíhou bù yào shuōhuà',
 'tā dǎ diànhuà gàosu wǒ, tā huì wǎn yī diǎnr dào',
 'lǎoshī zhèngzài gěi wǒmen jièshào xīn tóngxué',
 'nǐ zhǔnbèi shénme shíhou huí guó?',
 'Wǒ juéde zhè ge diànyǐng yī diǎnr dōu bù hǎo kàn',
 'wǒ xīwàng bàba māma shēntǐ jiànkāng',
 'jīntiān kěnéng huì xiàyǔ',
 'gēge shuō míngtiān jiào wǒ dǎ lánqiú',
 'cāochǎng shàng yǒu hěn duō háizi zài tī zúqiú',
 'Tā de yáchǐ fēicháng bái',
 'wàimiàn tài hēi le, wǒ shénme dōu kàn bù jiàn',
 'wǒ de hēi tóufa yuè lái yuè shǎo, bái tóufa yuè lái yuè duō',
 'nǐ de liǎn zěnme zhème hóng?',
 'Wǒmen de xīn línjū shì wàiguó rén',
 'zhè ge chéngshì nǎr dōu hǎo, jiù shì fángzi tài guì le',
 'nǐ wèi shénme mǎi zhème guì de shǒujī?',
 'Tā zài zhèr děng le nǐ hěn cháng shíjiān le',
 'zhè tiáo kùzi tài cháng le, yǒu duǎn yī diǎnr de ma?',
 'Shìjiè shang zuì gāo de lóu zài nǎ ge guójiā?',
 'Rénmen de shēnghuó shuǐpíng yuè lái yuè gāo le',
 'bàba gōngzuò hěn máng, měitiān dōu hěn wǎn huí jiā',
 'wǒ huàn le xīn gōngzuò, bǐ yǐqián gèng máng le',
 'zhè ge zì nǐ xiě cuò le, yīnggāi zhè yàng xiě',
 'nǐ zhīdào nǐ nǎli zuò cuò le ma?',
 'Wǒ jiā hé tā jiā lí de hěn jìn (alternative: 我家离他家很近)',
 'nà jiā fàndiàn tài yuǎn le, wǒmen zhǎo yī jiā jìn yī diǎnr de ba',
 'zhèr lí huǒchē zhàn yǒu duō yuǎn? 这儿离火车站远吗？  这儿离火车站远不远？',
 'Lí wǒ jiā bù yuǎn de dìfang yǒu yī jiā yīyuàn',
 'nǐ kuài yī diǎnr, huǒchē yào kāi le',
 'lǎoshī shuō de tài kuài le, wǒ méi tīng qīngchu (hear + understand)',
 'wài mian zhèng zài xià yǔ, nǐ kāi chē de shíhou màn yī diǎnr',
 'wǒmen zǒu de hěn màn, zǒu le hěn jiǔ cái dào jiā',
 'jīntiān shì qíngtiān, wǒmen yīqǐ chū qù wánr ba',
 'jīntiān shì yīntiān, yǒudiǎnr lěng',
 'wǒmen bān yǒu yī ge yòu gāo yòu shuài de nán tóngxué',
 'wǒ zài nǚ cèsuǒ mén qián jiǎn dào le yī ge qiánbāo',
 'zhè ge miànbāo tài hǎo chī le, wǒ xiǎng zài chī yī ge',
 'wǒ dǎ yǔmáoqiú dǎ de hái kěyǐ',
 'zhè ge diànyǐng hái kěyǐ, nǐ kěyǐ qù kàn yī xià',
 'huǒchē piào bǐ fēijī piào gèng piányi',
 'nǎli néng mǎi dào yòu hǎo chī yòu piányi de shuǐguǒ?',
 'Hé nǐ liáotiān wǒ juéde hěn kuàilè',
 'wǒ yào gěi dàjiā dōu jiǎng yī ge gùshi',
 'zhè ge huódòng měi ge rén dōu bìxū cānjiā',
 'nà běn shū nǐ kàn wán le ma? Nǐ shénme shíhou bǎ tā huán gěi wǒ?',
 'Tāmen wèishénme zhème gāoxìng?',
 'Gēge zhèng zài xuéxí, nǐ bié dǎrǎo tā',
 'nǐ bié hē jiǔ, yī huìr hái yào kāi chē ne',
 'zhè jiàn shì nǐ zuò de fēicháng hǎo',
 'wǒmen rènshi jiǔ nián le, wǒ fēicháng liǎojiě tā',
 'zhè jiàn yīfu hái bù cuò',
 'wǒ hái xiǎng qù yī cì běijīng',
 'nǐ hái zài nà ge gōngsī shàng bān ma?',
 'Nǐ néng bù néng zài shuō yī biàn?',
 'Nǐ bié zài gěi wǒ dǎ diànhuà le',
 'zhè tào xīzhuāng háishì tài xiǎo le, yǒu méi yǒu zài dà yī diǎnr de?',
 'nǐ xiě wán zuòyè zài kàn diànshì',
 'wǒ xiān xiǎng xiǎng zài huídá nǐ',
 'zhè shuāng xiézi hái bù cuò, jiù mǎi zhè shuāng ba',
 'lóu xià yǒu ge chāoshì, jiù qù nàli mǎi yī diǎnr cài ba',
 'wǒ jīntiān wǔ diǎn zhōng jiù qǐchuáng le',
 'tā yīshíwǔ suì jiù jiéhūn le',
 'wǒmen yǐjīng yī nián méi yǒu jiànmiàn le',
 'nǐ lái wǎn le, tā yǐjīng huí qù le',
 'wáng jīnglǐ zhèngzài kāihuì',
 'nǎinai zhèngzài xuéxí yòng shǒujī shàng wǎng',
 'zhè zhēn shì yī ge hǎo bànfǎ',
 'dú wán zhè běn shū zuì shǎo xūyào yī ge xīngqī',
 'zhè shì wǒmen bān chéngjī zuì hǎo de xuéshēng',
 'hěn duō rén cānjiā le zhè ge huódòng',
 'tā yī ge xīngqī qù kàn liǎng cì diànyǐng',
 'bǎoluó yǐjīng liǎng ge yuè méi lái shàng hànyǔ kè le',
 'tā zhè cì kǎoshì kǎo le yī bǎi fēn',
 'zhè ge gōngsī yǒu jǐ qiān ge rén',
 'wǒ huā le bā kuài qián mǎi le yī bǎ huā',
 'nǐ jīntiān dì yī tiān qù shàng bān, qiānwàn bié chí dào le',
 'wǒ zài gěi nǐ yī cì jīhuì',
 'wǒ tūrán xiǎng qǐlái yī jiàn shìqing',
 'tā gāngcái pāi le wǒ yī xià',
 'nǐ zài zhèr děng yī xià, wǒ mǎ shàng huí lái',
 'qǐng nǐ bāng wǒ ná yī xià wǒ de bāo',
 'tā chàng gē chàng de hěn hǎo tīng (alternativa: 她歌唱得很好听)',
 'nǐ zhǎo wǒ yǒu shì ma? Wǒ zhèng máng zhe ne',
 'wǒ jīnnián bǐ qùnián pàng le',
 'nǐ shì cóng nǎli lái de?',
 'Nǐ yǒu shénme huà xiǎng duì wǒ shuō ma?',
 'Nǐ yào duì zìjǐ yǒu xìnxīn',
 'qǐngwèn fēi wǎng běijīng de fēijī qǐfēi le ma?',
 'Qǐngwèn fēi wǎng shànghǎi de fēijī jiàngluò le ma?',
 'Suīrán zhè tiáo qúnzi hěn guì, dàn tā háishi mǎi le',
 'suīrán gōngzuò hěn máng, dànshì wǒ yī zhí jiānchí xuéxí hànyǔ',
 'yīnwèi tā shēng bìng le, suǒyǐ tā jīntiān méi lái',
 'nǐ hái zài yīnwèi nà jiàn shìqíng shēngqì ma?',
 'Nǐ hái xiǎo, suǒyǐ nǐ bù dǒng'],
    'Column3': ['My grandfather often lets me read the newspaper for him',
 '(Alguien pregunta antes: ¿dónde has leído esta revista?)  He leído (completamente) esta noticia en el periódico',
 'Pencil is not allowed to be used during the exam',
 'My mother bought a new watch for me',
 'She took some photos for me with her cell phone',
 'Please everyone switch off cell phones during the meeting',
 'This park needs no entrance tickets',
 'He went to the train station to buy tickets for the train',
 'Please help me to open the door',
 'Somebody is outside knocking at the door',
 'You should take medicine if you got ill',
 'Take this medicine three times a day',
 'We can go to the library by bus',
 'He is a bus driver',
 'This road is not good',
 'Please stop at the road side',
 'Do not drink too much coffee, for your health',
 'I am going to the supermarket to buy milk',
 'Is there any milk left in the fridge?',
 'Watermelons from this supermarket are both tasty and cheap',
 'How many eggs can be bought with 10 CNY?',
 'People in the North like to eat noodles',
 'People in the South like to eat rice',
 'My mother cooked a bowl of noodles for me',
 'Have you ever eaten hot pot of lamb?',
 'You should take very good care of these fishes while I am out of home',
 'My wife has a pair of beautiful brown eyes',
 'Close your eyes, rest for a while',
 'How are you feeling lately? (literal: how is your body recently?)',
 'Will it snow this winter?',
 "Grandmother's hair is white like snow",
 'This exam/test is simple',
 "You can certainly pass tomorrow's exam",
 'We have class at 8:00 every morning',
 'I quite like (to attend) Chinese class',
 'How do you do this math problem?',
 'There are four questions in this exam in total',
 'Please answer my question',
 'There is something wrong with my cell phone',
 'The doctor told me I should do more sport',
 'Swimming is a good sport to keep fit',
 'What is the colour of her eyes?',
 'How many kinds of colours does this piece of clothes have?',
 'He has been ill for a long time',
 'There is no time, hurry up',
 'There is a park beside Confucius Institute',
 'I want to sit by the window',
 'Go straight ahead, the library is on your right',
 'When crossing the road, look first at the left, then look at the right',
 'The elevator on the right is broken, let us take the one on the left',
 'You stand to the left for a while',
 'A new car stopped outside the door',
 'The Manager Wang is abroad now',
 'We (have to) work eight hours a day',
 'You already have been late for one hour',
 'I bought this shirt last year',
 'I just graduated last year',
 'What did you eat this morning?',
 'She is used to doing exercise early in the morning',
 'Do not call me after 9 pm',
 'Monday to Friday are working days',
 'Christmas is on December 25th every year',
 'I just finished to celebrate my 33rd birthday',
 'The birthday of my mother and father are the same day',
 'I look like my father, my younger brother looks like my mother',
 'I really wish I had a new car',
 'My elder sister and I study in the same school',
 'My younger sister is losing weight recently',
 'Elder sister is a bit taller than younger sister',
 'Mum asked me to take care of my younger brother and sister',
 'I love my wife',
 'I am hungry because I did not eat breakfast today',
 'She decided to divorce from her husband',
 'The husband is four years older than the wife',
 'They got married ten years ago, and still have no children',
 'All children like candy',
 'The waiters in this restaurant are very cordial',
 'Waiter, take two bottles of beer',
 'I have a lot of things to do',
 'This thing is not that simple',
 'What is the meaning of this word?',
 'I understand what you mean (now)',
 'Excuse me one second, how do I go to this guesthouse (hotel)?',
 'She lives in a guesthouse (hotel) near the company',
 'I asked for a leave of absence, I will not go to the company tomorrow',
 'He went to the train station to pick up his girlfriend',
 'It takes an hour to go to the airport from here',
 'Things at airport are usually expensive',
 'This hotel has sixty nine rooms in total',
 'I finally have my own room',
 'Our classroom is on the third floor',
 'Children are studying seriously in the classroom',
 'Today is very very cold, I do not want to go out',
 'I wait at home for my mother to come back to cook',
 'What present are you planning to give/present her for her birthday?',
 'I am also unable to solve this problem, go ask the teacher',
 'Remember to wash dishware after finishing to eat',
 'Dad smiled while telling us stories of his youth',
 'Have you already found a new job?',
 'I still search for new job',
 'Go a bit faster, we are going to arrive delayed',
 'If you arrive, you order food first',
 'All the other people know, only you still do not understand',
 'May I ask your family name?',
 'My home is near from school',
 'I finally finished reading this book',
 'Where would you like to go today (for fun)?',
 'Let us begin to study now',
 'I decided to start from tomorrow to learn how to cook',
 'The weather is very cold, I do not want to get up at all',
 'Many middle-aged and elderly people like to go dancing in the square after dinner',
 'I am so busy recently that I even have no time to go to travel',
 'He goes to work by bike every day',
 'The doctor said he needs a rest',
 'Do not remain seated all the time, stand up (at once) and do some exercise',
 'Every day after getting up he goes to run in the park',
 'I am recently learning to swim',
 'I heard you were ill, are you a bit better now?',
 'Do not talk during class',
 'She called to tell me that she will arrive a bit late',
 'The teacher is introducing right now new classmates to us',
 'When do you plan to return to the country?',
 'I think this movie is not good at all',
 'I hope my parents are healthy (literal: body of my parents healthy)',
 'Perharps it will rain today',
 'My eldest brother said he will teach me tomorrow to play basketball',
 'There are many children playing football in the playground',
 'His teeth are very white',
 'It is so dark outside, I cannot see anything',
 'My dark hair is lesser and lesser, my white hair is more and more',
 'Why is your face so red?',
 'Our new neighbours are foreigners',
 'This town is good everywhere, just for this houses are too expensive',
 'Why do you buy such an expensive mobile phone?',
 'He has been waiting here for you for a long time',
 'This pair of trousers is too long, do you have one a bit shorter?',
 'In which country is the tallest building in the world?',
 "People's standard/level of living is getting higher and higher",
 "Dad's work is quite busy, he comes home late every day",
 'I changed to a new job, I am even busier than before',
 'You wrote the character wrong, it should be written like this',
 'Do you know what you did wrong?',
 'My home is near his home',
 'That restaurant is too far away, let us find a closer one',
 'How far is it from here to the train station?',
 'There is a hospital not far from my home',
 'Hurry up, the train is about to leave',
 'The teacher spoke so fast that I did not hear clearly',
 'Outside it is raining, when you drive go a bit slowly',
 'We walked so slowly that we walked a long time to arrive home just now',
 'It is sunny today, let us go out together to play',
 'It is cloudy today, it is a bit cold',
 'There is a tall, handsome male classmate in our class',
 "I picked up/collected a wallet in from of the ladies' toilet",
 'This bread is so delicious that I want eat one again',
 'I am not bad at badminton',
 'This movie is not bad, you can go watch it',
 'Train tickets are even cheaper than flight tickets',
 'Where can I buy fruit both tasty and cheap?',
 'I feel happy for chatting with you',
 'I am going to tell all of you a story',
 'Everybody (each one) must take part in this activity',
 'Have you finished reading that book? When will you return it to me?',
 'Why are they so happy?',
 'Your elder brother is studying right now, do not disturb him',
 'Do not drink (alcohol), you will drive in a while/later',
 'You did a good job / What you did was very good',
 'We have known each other for more than nine years, I know her very well',
 'This piece of clothes is fairly OK/not bad',
 'I still want to go one more time to Peking',
 'Do you still work in that company?',
 'Can you say it once again?',
 'Do not call me again',
 'This suit is still too small, do you have a larger one?',
 'Do you homework, then watch TV',
 'I will think a bit first, then I will answer you',
 'This pair of shoes is fairly good, then let us buy it',
 'There is a supermarket downstairs, then go there and buy some food',
 "I got up at at five o'clock today (remark: usually I wake up later, toda it went earlier or fast and well)",
 'She got married when she was fifteen (remark: speaker thinks it was early)',
 'It is already one year we do not meet',
 'You arrived late, he went back already',
 'Manager Wang is in a meeting right now',
 'Grandmother is right now learning to surf the internet with her mobile phone',
 'It is really a good idea (literal: method)',
 'You need at least one week to finish reading this book',
 'This is the best student in our class (literal: with best grades/performance records)',
 'Many people took part in this activity / event',
 'She goes to the movies twice a week',
 'It is already two months that Pablo does not come to Chinese class',
 'He got one hundred points on this exam',
 'This company has several thousands of people',
 'I spent eight CHY to buy a bunch of flowers',
 "Today is the first day you go to work, make sure you don't arrive delayed",
 'I give you another chance',
 'I suddenly remembered one thing (a thing came up to my mind)',
 'He claped me once just now',
 'Wait here for a moment, I will come back immediately',
 'Please help me take my bag for a moment',
 'She sings very well',
 'What are you looking for me for? I am busy now',
 'I am fatter than last year',
 'Where do you come from?',
 'Is there anything you want to tell me?',
 'You should have confidence in yourself',
 'Excuse me: the plane which flies to Peking has already taken off?',
 'Excuse me: the plane from the flight to Shanghai has already landed?',
 'Although this skirt is expensive, yet she still bought it',
 'Although very busy at work, yet I always insist in learning Chinese',
 'She does not come today because she is sick',
 'Are you still angry because of that matter?',
 'You are still young to understand']
})


# Page configuration
st.set_page_config(
    page_title='Google',
    page_icon='https://www.google.com/favicon.ico',
    layout='wide')

######
st.write('HSK 2')

#st.dataframe(df.sample(3)) # Optional, to show dataframe

# Initialize or update the session state to store the random row index
if "random_index" not in st.session_state:
    st.session_state.random_index = random.randint(0, len(df) - 1)

# Function to pick a new random row
def get_new_random_row():
    st.session_state.random_index = random.randint(0, len(df) - 1)

# Get the current random row
random_row = df.iloc[st.session_state.random_index]

# Display the value of the first column
#st.title("?")
st.title(random_row.iloc[0])

####################################################

# Detect keypress
key = keypress()

# Spacebar shortcut for the '???' button
if key == " " or st.button('???'):
    st.subheader(random_row.iloc[1])  # Display value from Column 2
    st.subheader(random_row.iloc[2])  # Display value from Column 3

# Right arrow shortcut for the '+++' button
if key == "ArrowRight" or st.button("+++"):
    get_new_random_row()  # Generate a new random row
    st.experimental_rerun()  # Refresh the app


####################################################

# Button to reveal values of the second and third columns
if key == " " or st.button('???'):
    #st.write(' ')
    #st.write("### Value from Column 2:")
    st.subheader(random_row.iloc[1])
    #st.write(' ')
    #st.write("### Value from Column 3:")
    st.subheader(random_row.iloc[2])

# Button to select a new random row
if key == "ArrowRight" or st.button("+++"):
    get_new_random_row()
    st.rerun()  # Refresh the app to display the new random row

