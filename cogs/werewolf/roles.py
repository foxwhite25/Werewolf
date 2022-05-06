from __future__ import annotations

import dataclasses
import random
from typing import Literal, List, Optional, Dict, Any

__all__ = (
    'Parties',
    'Role',
    'ROLES'
)

Parties = Literal['Thief', 'Village', 'Wolf', 'Tanner', 'Cult', 'SerialKiller', 'Arsonist']
Roles = Literal[
    'Villager', 'Drunk', 'Harlot', 'Seer', 'Traitor', 'GuardianAngel', 'Detective', 'Wolf', 'Cursed', 'Gunner',
    'Tanner', 'Fool', 'WildChild', 'Beholder', 'ApprenticeSeer', 'Cultist', 'CultistHunter', 'Mason', 'Doppelganger',
    'Cupid', 'Hunter', 'SerialKiller', 'Sorcerer', 'AlphaWolf', 'WolfCub', 'Blacksmith', 'ClumsyGuy', 'Mayor', 'Prince',
    'Lycan', 'Pacifist', 'WiseElder', 'Oracle', 'Sandman', 'WolfMan', 'Thief', 'Troublemaker', 'Chemist', 'SnowWolf',
    'GraveDigger', 'Augur', 'Arsonist'
]


@dataclasses.dataclass(frozen=True)
class Role:
    emoji: str
    name: str
    desc: List[str]
    about: str
    party: Parties
    eaten: Optional[str] = None
    killed: Optional[str] = None
    frozen: Optional[str] = None
    bit: int = 0
    strength: int = 0

    def __repr__(self):
        return f'<Role name={self.name} emoji={self.emoji}>'


class _RoleSentinel:
    Villager = Role(
        emoji="👱", name="村民",
        desc=[
            "你不过是一个普通村民罢了，不过不用管那么多，来一盘昆特牌怎么样？",
            "你不过是一个普通村民罢了，难道你觉得自己会有什么超能力吗？",
            "你不过是一个普通村民罢了，机智一点，好好利用手中的票！",
            "你不过是一个普通村民罢了，靠耕田自给自足度日的普通人。"
        ],
        about="你不过是普通村民，靠耕田自给自足度日的普通人。每天有一次机会通过投票处决一个人（有可能是狼人）。",
        party='Village', bit=1, strength=1
    )
    Drunk = Role(
        emoji="🍻", name="酒鬼",
        desc=[
            "你是众所周知的酒鬼！"
        ],
        about="你是个酒鬼，除此之外你和村民没什么区别。不过如果狼人杀了你，明晚他就杀不了别人，因为他也醉了。",
        eaten="大家一觉睡醒，扑鼻而来的是浓烈的酒精味，渗杂着烧焦的木屑味道 —— 此刻酒吧烧成一片火海！"
              "村民将火扑灭后，发现一具残缺的焦尸 —— %s 。",
        killed="村民们去找 %s 买酒喝的时候，发现他的尸体躺在一堆绝世好酒中间，被切了腹……【酒鬼 🍻】被谋杀了。",
        party='Village', bit=2, strength=3
    )
    Harlot = Role(
        emoji="💋", name="妓女",
        desc=[
            "你是妓女。你可以在晚上去其他人的家里谋取生计，顺便看看他们是不是狼人。不过，如果你刚好去的是狼人家，或者与狼人共处一室，"
            "你就会被狼人吃掉。如果你刚好外出而狼人要杀掉你的话，你可以逃过一劫。"
        ],
        about="你是妓女。你可以在晚上去其他人的家里谋取生计，顺便看看他们是不是狼人。"
              "不过，如果你刚好去的是狼人家，或者与狼人共处一室（去了狼人想吃掉的人的家里），你就会被狼人吃掉。"
              "如果你刚好外出而狼人要杀掉你的话，你可以逃过一劫。（因为你不在家）还有，偶尔你会隐隐约约看到邪教徒的祭坛。",
        eaten="妓女 %s 呆在家里没有出去，然后......被狼人吃掉了。",
        frozen="当你刚出门，进行调查时，一阵寒风，把你冻住了。",
        party="Village", bit=3, strength=6
    )
    Seer = Role(
        emoji="👳", name="先知",
        desc=[
            "你是先知。每当夜深人静时，你就可以预知其中一个玩家的身份。"
        ],
        about="你是先知。每当夜深人静时，你就可以预知其中一个玩家的身份。除非你希望被狼人杀掉，不要暴露你的身份！",
        eaten="村民们一觉醒来，看到广场中间被打碎的水晶球与被撕破的塔罗牌，而旁边是 %s 的尸体 —— 他是先知！",
        killed=" %s 被发现的时候，内脏被抛弃在水晶球的碎片中……【先知 👳】被谋杀了。",
        party="Village", bit=4, strength=7
    )
    Traitor = Role(
        emoji="🖕", name="叛徒",
        desc=[
            "你是叛徒。此刻你还是村民，如果所有狼人都死了，你就会成为狼人。作为叛徒，先知也有可能会把你当成真的狼人。",
        ],
        about="你是叛徒。此刻你还是村民，如果所有狼人都死了，你就会成为狼人。转而向你曾经的队友展开屠杀！"
              "不过作为叛徒，先知也有可能会把你当成真的狼人。",
        party="Village", bit=5, strength=0
    )
    GuardianAngel = Role(
        emoji="👼", name="守护天使",
        desc=[
            "你是守护天使。每当夜幕降临，你可以保护一名玩家免受生命威胁。但是，如果你保护了狼人，你有一半的几率会死。"
        ],
        about="你是守护天使。每当夜幕降临，你可以保护一名玩家免受生命威胁。但是，如果你保护了狼人，你有一半的几率会死。",
        frozen="昨夜，当你正打算出门守护时，发现门好像冻住了。你只能待在家。",
        party="Village", bit=6, strength=7
    )
    Detective = Role(
        emoji="🕵", name="侦探",
        desc=[
            "你是一名侦探。你可以在白天调查一名玩家的身份。但调查时，狼人们可能会发现你是侦探（40%的几率）。",
        ],
        about="你是一名侦探。你可以在白天调查一名玩家的身份，不过要小心的选择调查的目标！调查时，狼人们有40%的机率会发现你是侦探。",
        eaten="一大早，村民们聚首一堂，发现不见 %s 的踪影。大家在 %s 的屋子四周搜寻，"
              "然后在他家门前见到一具尸体：肚破肠流，还有个狼牙印赫然覆盖在尸体的喉咙处。",
        party="Village", bit=7, strength=7
    )
    Wolf = Role(
        emoji="🐺", name="狼人",
        desc=[
            "你是狼人！每晚你都可以大开杀戒！"
        ],
        about="你是狼人！每晚你都可以大开杀戒！不过如果你咬到了酒鬼，你会因为醉酒而在下回合无法行动。"
              "如果你咬到了被诅咒的人，他也会变成狼人，准备好欢迎你的新队友吧！",
        party="Wolf", bit=8, strength=10
    )
    Cursed = Role(
        emoji="😾", name="被诅咒的人",
        desc=[
            "你是被诅咒的人。现在你还是村民，但当狼人咬你之后，你就会变成狼人。"
        ],
        about="你是被诅咒的人。现在你还是村民，但当狼人咬你之后，你就会变成狼人。准备好加入杀戮了么？",
        party="Village", bit=9, strength=0
    )
    Gunner = Role(
        emoji="🔫", name="枪手",
        desc=[
            "你是枪手，拥有两颗子弹。你可以在白天射杀一名玩家。不过在你射出第一枪以后，所有人都会看到你开枪杀人。"
        ],
        about="你是枪手，拥有两颗子弹。你可以在白天射杀一名玩家。不过在你射出第一枪以后，所有人都会看到你开枪杀人。",
        eaten="村民们走出家门，发现满地的枪械零件，还有残肢、手指...广场上散布着血肉模糊的尸骸 —— 枪手 %s 已经死于狼爪之下！",
        killed=" %s 被人发现的时候，已经被自己的枪爆了头，身上还有和杀手撕打的痕迹。【枪手 🔫】被谋杀了。",
        party="Village", bit=10, strength=6
    )
    Tanner = Role(
        emoji="👺", name="皮匠",
        desc=[
            "你是皮匠。只要你被村民处决，你就是本场游戏的赢家。"
        ],
        about="你是皮匠。你的赢法非常简单：只要你被村民处决，你就是本场游戏的赢家。",
        party="Tanner", bit=11, strength=1
    )
    Fool = Role(
        emoji="🃏", name="冒牌先知",
        desc=[
            "你是先知。每当夜深人静时，你就可以预知其中一个玩家的身份。"
        ],
        about="你认为你是先知，但可惜你不是。当你去看他人的身份时，bot会随便告知你，比如你想看狼人的身份，bot却说他是守护天使。",
        eaten="村民们一觉醒来，看到广场中间被打碎的水晶球与被撕破的...UNO牌？！ %s 这货居然是个冒牌先知！",
        party="Village", bit=12, strength=3
    )
    WildChild = Role(
        emoji="👶", name="孤儿",
        desc=[
            "你是孤儿。可以选择一名玩家当你的偶像。但如果你的偶像死亡，你会变成狼人。"
        ],
        about="你是孤儿。可以选择一名玩家当你的偶像。但如果你的偶像死亡，你会变成狼人。",
        eaten="昨天晚上，狼群吃到了一顿嫩肉，这顿嫩肉是…… %s 。【孤儿 👶】被吃了。",
        party="Village", bit=12, strength=1
    )
    Beholder = Role(
        emoji="👁", name="旁观者",
        desc=[
            "你是旁观者，你知道谁是真正的先知。除此之外，你就是个普通人。"
        ],
        about="你是旁观者，你知道谁是真正的先知（不是冒牌先知，真的）。除此之外，你就是个普通人。",
        party="Village", bit=13, strength=1
    )
    ApprenticeSeer = Role(
        emoji="🙇", name="先知学徒",
        desc=[
            "你是先知学徒，一旦真正的先知死亡，你就会继承他们的使命。"
        ],
        about="你是先知学徒，一旦真正的先知死亡，你就会继承他们的使命，不过在这之前你还是个学徒（普通人）。",
        eaten="起床后，村民们发现 %s 被咬的只剩一副空皮囊，身旁还摆着一本《占卜术教程》，看来临死还挂念着学习……【先知学徒 🙇】被吃了。",
        party="Village", bit=14, strength=5
    )
    Cultist = Role(
        emoji="👤", name="邪教徒",
        desc=[
            "你是邪教徒。你可以在晚上施洗任意一名玩家，让他们成为你的一员。如果所有玩家都受洗成邪教徒，邪教徒就赢了。"
        ],
        about="",
        killed="%s 被发现被斩首在了奇怪的祭坛旁边……看来，信邪教得永生是一个骗局。【邪教徒 👤】被谋杀了。",
        frozen="当你开始准备邪教入会仪式事宜时，一阵风，把你冻住了。",
        party="Cult", bit=15, strength=10
    )
    CultistHunter = Role(
        emoji="💂", name="邪教捕手",
        desc=[
            "村里出现了邪教活动，所有人的思想自由都受到了威胁！作为邪教捕手，你的任务是每晚捕捉一名玩家，如果刚好是邪教徒，他就会死。"
            "如果有人想施洗你，最新加入的那位邪教徒就会死于非命。"
        ],
        about="作为邪教捕手，你的任务是每晚捕捉一名玩家，如果刚好是邪教徒，他就会死。如果有人想施洗你，最新加入的那位邪教徒就会死于非命。",
        killed="早上， %s 的尸体被发现，他平时带着的十字架，反而被刺进了他的太阳穴。。。【邪教捕手 💂】被谋杀了。",
        party="Village", bit=16, strength=7
    )
    Mason = Role(
        emoji="👷", name="共济会会员",
        desc=[
            "你是共济会会员。如有其他共济会会员同伴，你也会知道他们是谁。除此之外你就跟普通村民一样。"
        ],
        about="你是共济会会员。如有其他共济会会员同伴，你也会知道他们是谁。"
              "除此之外你就跟普通村民一样。不过如果同伴没来参加聚会，你就会知道他的身份变了，极有可能被洗成了邪教徒。\n",
        eaten="一大早，村民们在一堆石头中发现一具残破不堪满身血迹的尸体。村里的一名共济会会员死了！ -- %s",

        party="Village", bit=17, strength=1
    )
    Doppelganger = Role(
        emoji="🎭", name="替身",
        desc=[
            "你是替身。据传你的祖先是变形女，可以任意变形，而你继承了一部分的能力。选择一名玩家，当该玩家死后，你将接替他们的角色。"
        ],
        about="你是替身。据传你的祖先是变形女，可以任意变形，而你继承了一部分的能力。\n"
              "选择一名玩家，当该玩家死后，你将接替他们的角色。\n"
              "如果你选择的角色在受洗成邪教徒后死亡，你会接替他原有的角色。\n"
              "如果选的是是孤儿，他和偶像死了，你会变成狼人。\n"
              "如果孤儿死了，但他的偶像没死，你会继承孤儿的身份和他的偶像；你在变身前不会被洗成邪教徒，但变身后可以被洗。\n"
              "如果到最后都没有变形，那你就输了（除了你和另外一人是情侣）。\n",
        party="Village", bit=18, strength=2
    )
    Cupid = Role(
        emoji="💘", name="爱神",
        desc=[
            "你是爱神。带着一弓两箭就被送到了地球。你可以用箭射中两个玩家让他们成为情侣。如果一方死去，另一方伤心之下，会自杀殉情。"
        ],
        about="",
        killed="第二天，村民发现爱神的象征 %s 并没有受到护佑——他同样被杀手肢解了。【爱神 🏹】被谋杀了。",
        party="Village", bit=19, strength=2
    )
    Hunter = Role(
        emoji="🎯", name="猎人",
        desc=[
            "你是小镇的猎人。来福枪不在手上你就睡不踏实。如果你死了，你可以选择一名玩家和你陪葬。"
            "如果你被狼人咬了，那你有机会把这个狼人杀死，但却不能再选择杀死其他人。"
        ],
        about="你是小镇的猎人。来福枪不在手上你就睡不踏实。如果你死了，你可以选择一名玩家和你陪葬。"
              "如果你被狼人咬了，那你有机会把这个狼人杀死，但却不能再选择杀死其他人。\n"
              "如果其他人去你家，他们有可能因为你发疯而被你杀死；如果狼人来杀你，你有机会杀死他；你死前可以杀死一人跟你陪葬。\n"
              "狼人去你家的时候你杀他们的几率按游戏里的狼人数目而定：一只狼=30%，两只狼=50%，三只狼=70%，如此类推。"
              "（但是如果你遇上不止一只狼，你有机会杀死其中一只，却会因为不敌群狼而死。"
              "如果邪教徒来传教，他们有50%失败。一旦他们失败，你就有50%机会杀死他们中的一个。\n",
        party="Village", bit=20, strength=6
    )
    SerialKiller = Role(
        emoji="🔪", name="变态杀人狂",
        desc=[
            "你是变态杀人狂。最近刚从精神病院逃出来，想要杀死全镇的人。每晚你可以在你的死亡清单上添加一名玩家（包括狼人）。"
        ],
        about="你是变态杀人狂。最近刚从精神病院逃出来，想要杀死全镇的人。"
              "你可以杀任何人，就算狼人来杀你，你也会活着杀死其中一个。"
              "唯一的胜出方法是成为最后一个存活的玩家。（和某人成为情侣并取胜以外）",
        frozen="当你打算偷肾来氪金时,发现门好像冻住了。",
        party="SerialKiller", bit=21, strength=15
    )
    Sorcerer = Role(
        emoji="🔮", name="暗黑法师",
        desc=[
            "你是暗黑法师，属于狼人阵营中类似先知的存在；然而你的法力仅仅足以探知到狼人和先知，对其他的身份则无法感知。"
        ],
        about="暗黑法师，是狼人阵营如同先知一样的存在，然而法力不足，只能探测出狼人和先知这两种身份，其他一概不知。",
        eaten="“不要吃我，我是你们的人！”晚上突然传来这样一句话。第二天， %s 被吃剩下的骨头被发现了。【暗黑法师🔮】被吃了。",
        party="Wolf", bit=22, strength=2
    )
    AlphaWolf = Role(
        emoji="⚡", name="头狼",
        desc=[
            "你是头狼，是狼群精神力的源泉。只要你活着，被狼群咬死的人就有 20% 机率变狼。"
        ],
        about="头狼，乃是狼群的精神源泉，只要他还活着，被咬的人就有 20% 的机率免于死难——然而会变成狼人。",
        party="Wolf", bit=23, strength=12
    )
    WolfCub = Role(
        emoji="🐶", name="幼狼",
        desc=[
            "你是幼狼，狼群里备受呵护的下一代，就像早上七八点钟的太阳。"
            "如果你死了的话，愤怒的狼群下一晚会咬死两个人，用来祭奠你。"
            "虽然你还 Too young too simple，但是也已经身经百战，同样拥有每晚选择一位村民咬死的能力。"
        ],
        about="幼狼，是狼群的希望；如果幼狼死了的话，剩下的狼会在下一晚杀死两个人泄愤。",
        party="Wolf", bit=24, strength=10
    )
    Blacksmith = Role(
        emoji="⚒", name="铁匠",
        desc=[
            "你是铁匠，家里有一包祖传的防狼神器——银粉。在白天的时候，你可以把银粉绕村洒一圈，这样今晚狼人就没法吃人了。"
            "然而，因为是祖传的，所以只有一包，用了就没了。"
        ],
        about="铁匠，祖传一包防狼银粉，可以在白天洒在村子里，保证当天晚上村子不会出现狼人咬人的情况。",
        killed="看来 %s 昨晚倒霉出奇了……他的尸体，被发现的时候，已经被他自己的大锤砸烂了……【铁匠 ⚒】被谋杀了。",
        party="Village", bit=25, strength=5
    )
    ClumsyGuy = Role(
        emoji="🤕", name="粗心鬼",
        desc=[
            "你是粗心鬼，明明心里有想投的人，可是投票的时候，还是有 50% 的机率把选票写错，从而不小心让无辜的人躺枪。"
        ],
        about="粗心鬼，神经太大条了，勾选票的时候都有 50% 会勾错。",
        party="Village", bit=26, strength=-1
    )
    Mayor = Role(
        emoji="🎖", name="村长",
        desc=[
            "你是村长，在白天的时候，你可以把委任状拿出来表露身份；然后你的一票就相当于别人的两票了。"
        ],
        about="村长是上级镇政府委派管理这个村子的，"
              "白天的时候，可以选择把委任状拿出来，这样村民就会承认身份，于是村长就拥有了一票顶别人两票的权力。",
        killed="我村伟大的领导人 %s 于昨晚死于谋杀，凶手尚未查明。党和中央对此表示极大哀悼。【村长 🎖】被谋杀了。",
        party="Village", bit=27, strength=4
    )
    Prince = Role(
        emoji="👑", name="王子",
        desc=[
            "你是王子，当你将被乱民处死的那一刻，他们会发现你的身份，认识到自己的错误，饶你一命。"
            "可是，如果他们执意想投你，你也只能怨恨父王没能好好管教他的子民了。"
        ],
        about="王子是当今国王的儿子。当王子被第一次投票准备处决的时候，可以凭借此身份躲过一难。",
        killed="昨晚御用保镖旷工，赶到王子 %s 家前的时候，只看到了一地尸体……【王子 👑】被谋杀了。",
        party="Village", bit=28, strength=3
    )
    Lycan = Role(
        emoji="🐺🌝", name="狼人(潜隐者)",
        desc=[
            "你是普通狼人，但经过多年隐匿，逐渐学会隐藏自己踪迹的能力，现在你可以不被👳先知发现你的身份。"
        ],
        about="🐺狼人( 潜隐者 )，普通狼人，但经过多年隐匿，逐渐学会隐藏自己踪迹的能力，现在可以不被👳先知发现你的身份。",
        party="Wolf", bit=29, strength=10
    )
    Pacifist = Role(
        emoji="☮", name="和平演说者",
        desc=[
            "你是和平演说者，你可以选择进行一次和平演说，劝说所有人不投票处决一次。"
        ],
        about="和平演说者\n可以选择进行一次和平演说，劝说所有人不投票处决一次（仅一次）",
        party="Village", bit=30, strength=3
    )
    WiseElder = Role(
        emoji="📚", name="长老",
        desc=[
            "你是长老，苍老但睿智。\n你可以躲避🐺狼人的一次攻击（仅一次）。\n"
            "如果枪手或猎人杀死了你，出于慈悲，他们都会后悔，失去他们的能力，变成普通村民。"
        ],
        about="长老，苍老但睿智。\n你可以躲避🐺狼人的一次攻击（仅一次）。\n"
              "如果枪手或猎人杀死了你，出于慈悲，他们都会后悔，失去他们的能力，变成普通村民。",
        party="Village", bit=31, strength=3
    )
    Oracle = Role(
        emoji="🌀", name="神谕",
        desc=[
            "你是🌀神谕，每天晚上你可以知道一个人（只能是活人）不是什么身份。"
        ],
        about="🌀神谕，每天晚上你可以知道一个人（只能是活人）不是什么身份。",
        party="Village", bit=32, strength=4
    )
    Sandman = Role(
        emoji="💤", name="睡神",
        desc=[
            "你是💤睡神，可以催眠一切生物，让所有人入睡，夜间不再活动。（仅一次）"
        ],
        about="💤睡神，可以催眠一切生物，让所有人入睡，夜间不再活动。",
        party="Village", bit=33, strength=3
    )
    WolfMan = Role(
        emoji="👨🌚", name="“狼”人",
        desc=[
            "你是“狼”人--村民，但由于你经常在树林里，似乎👳先知把你当🐺狼人看。"
        ],
        about="“狼”人--村民，但由于经常在树林里，似乎👳先知把他当🐺狼人看。",
        party="Village", bit=34, strength=1
    )
    Thief = Role(
        emoji="👻", name="小偷",
        desc=[
            "你是👻小偷！\n 小偷模式-默认：👻小偷第一晚可以偷取某人能力，且被偷取能力的玩家将变成普通村民。",
            "你是👻小偷！\n  小偷模式-完整：👻小偷每晚可以偷取某人能力，有50%几率成功，如果成功，则被偷取能力的玩家 将变成👻小偷。"
            "（其实就是交换能力.）"
        ],
        about="小偷模式-默认：👻小偷第一晚可以偷取某人能力，且被偷取能力的玩家将变成普通村民\n"
              "小偷模式-完整：👻小偷每晚可以偷取某人能力，有50%几率成功，如果成功，则被偷取能力的玩家 将变成👻小偷。"
              "（其实就是交换能力）",
        frozen="昨夜，当你正打算出门偷他人能力时，发现门好像冻住了。",
        party="Thief", bit=35, strength=0
    )
    Troublemaker = Role(
        emoji="🤯", name="捣乱者",
        desc=[
            "你是🤯捣乱者，小镇里的无业青年，经常闹事情。当你捣乱时，整个村都炸了。因此，那天要投票处决两次!"
        ],
        about="🤯捣乱者，小镇里的无业青年，经常闹事情。当他们捣乱时，整个村都炸了。因此，那天要投票处决两次!",
        party="Village", bit=36, strength=5
    )
    Chemist = Role(
        emoji="👨‍🔬", name="疯狂化学家",
        desc=[
            "你是疯狂化学家👨‍🔬，你拥有两片药，一片毒药，一片是糖。"
            "每当夜晚，你会拜访一个人，会强制让人随机吞服其中一片，而你吞服另一片。"
        ],
        about="疯狂化学家👨‍🔬你拥有两片药，一片毒药，一片是糖。"
              "每当夜晚，你会拜访一个人，会强制让人随机吞服其中一片，而你吞服另一片。所以，祝你好运。",
        party="Village", bit=37, strength=0
    )
    SnowWolf = Role(
        emoji="🐺☃️", name="雪狼",
        desc=[
            "你是雪狼：源自雪山，特立独行。拥有冻结他人夜间能力的能力，但不久后他们将对你免疫，你不再能冻结他的能力了。"
        ],
        about="雪狼：源自雪山，特立独行。拥有冻结他人能力的能力，但不久后他们将对你免疫，不再能冻结他的能力了。",
        party="Wolf", bit=38, strength=15
    )
    GraveDigger = Role(
        emoji="☠️", name="掘墓人",
        desc=[
            "你是☠️掘墓人：\n"
            "1.每天晚上，你为上次死去的所有人挖掘坟墓，因此你整晚都在外面，狼和邪教会等找不到你\n"
            "2.除非那天没有人死亡 ,在这种情况下你只会待在家里，狼人和邪教会等可以找到你\n"
            "3.每个访问你的人都有可能掉进你新挖的坟墓里，这取决于你挖了多少坟墓\n"
            "4.此外，守护天使，妓女，邪教捕手 掉进你挖的坑（雾）的机会将减半\n"
            "5.但是因为你晚上外出，🐺狼人或🔪变态杀人狂可能会在墓地发现并杀死你，且你挖掘的坑（划去）坟墓越多，就越有可能被发现\n"
            "6.此外，变态杀人狂无论你在不在家都可以找到你，"
            "但他会在你的一个坟墓中绊倒并负伤，导致他有一半几率在第二天晚上失去杀人对象的决定权...\n"
        ],
        about="☠️掘墓人：\n"
              "1.每天晚上，你为上次死去的所有人挖掘坟墓，因此你整晚都在外面，狼和邪教会等找不到你\n"
              "2.除非那天没有人死亡 ,在这种情况下你只会待在家里，狼人和邪教会等可以找到你\n"
              "3.每个访问你的人都有可能掉进你新挖的坟墓里，这取决于你挖了多少坟墓\n"
              "4.此外，守护天使，妓女，邪教捕手 掉进你挖的坑（雾）的机会将减半\n"
              "5.但是因为你晚上外出，🐺狼人或🔪变态杀人狂可能会在墓地发现并杀死你，且你挖掘的坑（划去）坟墓越多，就越有可能被发现\n"
              "6.此外，变态杀人狂无论你在不在家都可以找到你，"
              "但他会在你的一个坟墓中绊倒并负伤，导致他有一半几率在第二天晚上失去杀人对象的决定权...\n",
        frozen="当你准备离开你家，去为那些死去的村民挖掘坟墓时，一阵风，似乎把你你家的房子冻住了...似乎，今天死者可能要再等一天了...",
        party="Village", bit=39, strength=8
    )
    Augur = Role(
        emoji="🦅", name="占卜者",
        desc=[
            "你是🦅占卜者，每天早上，你观察早霞的颜色和云彩变化，以及物象，预知村子里没有的角色。提示：每个不存在的角色只会告诉你一次。"
        ],
        about="🦅占卜者，每天早上，你观察早霞的颜色和云彩变化，以及物象，预知村子里没有的角色。提示：每个不存在的角色只会告诉你一次。",
        party="Village", bit=40, strength=5
    )
    Arsonist = Role(
        emoji="🔥", name="纵火犯",
        desc=[
            "你是纵火犯.，你孤身一人。你每天可以对别人家的房子浇汽油，然后在另一天放一把火，一起烧掉。"
        ],
        about="纵火犯，孤身一人。每天可以对别人家的房子浇汽油，然后在另一天放一把火，一起烧掉。",
        party="Arsonist", bit=41, strength=8
    )

    @property
    def all_role(self) -> Dict[Roles, Role]:
        return {m: n for m, n in _RoleSentinel.__dict__.items() if isinstance(n, Role)}

    @property
    def village(self) -> Dict[Roles, Role]:
        return {m: n for m, n in _RoleSentinel.__dict__.items() if isinstance(n, Role) and n.party == "Village"}

    @property
    def wolf(self) -> Dict[Roles, Role]:
        return {m: n for m, n in _RoleSentinel.__dict__.items() if isinstance(n, Role) and n.party == "Wolf"}

    @property
    def not_wolf(self) -> Dict[Roles, Role]:
        return {m: n for m, n in _RoleSentinel.__dict__.items() if isinstance(n, Role) and n.party != "Wolf"}

    @property
    def evil(self) -> Dict[Roles, Role]:
        return {m: n for m, n in _RoleSentinel.__dict__.items() if isinstance(n, Role) and n.party in [
            "Wolf", 'Cult', 'SerialKiller', 'Arsonist'
        ]}

    @property
    def not_evil(self) -> Dict[Roles, Role]:
        return {m: n for m, n in _RoleSentinel.__dict__.items() if isinstance(n, Role) and n.party not in [
            "Wolf", 'Cult', 'SerialKiller', 'Arsonist'
        ]}

    @property
    def not_evil_list(self) -> List[Role]:
        return [n for m, n in _RoleSentinel.__dict__.items() if isinstance(n, Role) and n.party not in [
            "Wolf", 'Cult', 'SerialKiller', 'Arsonist'
        ]]

    @property
    def evil_list(self) -> List[Role]:
        return [n for m, n in _RoleSentinel.__dict__.items() if isinstance(n, Role) and n.party in [
            "Wolf", 'Cult', 'SerialKiller', 'Arsonist'
        ]]

    @staticmethod
    def has_role(bit: int, role: Role):
        return not not bit & (1 << role.bit)


ROLES = _RoleSentinel()
