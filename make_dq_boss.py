import json

str = [
    {
        "BossName": "竜王",
        "AppearanceWork": "DQ1",
        "Lines": "「もし わしの みかたになれば せかいの はんぶんを 〇〇に やろう。」",
        "status": {
            "HP": 350,
            "MP": 0,
            "Attack": 130,
            "Defence": 150,
            "Speed": 90
        }
    },

    {
        "BossName": "ハーゴン",
        "AppearanceWork": "DQ2",
        "Lines": "「誰じゃ？私の祈りをじゃまする者は？おろかものめ！私を大神官ハーゴンと知ってのおこないか！？」",
        "status": {
            "HP": 460,
            "MP": 255,
            "Attack": 177,
            "Defence": 165,
            "Speed": 150
        }
    },

    {
        "BossName": "シドー",
        "AppearanceWork": "DQ2",
        "Lines": "「グギャアアアアァァァァッ!!!」",
        "status": {
            "HP": 1750,
            "MP": 255,
            "Attack": 235,
            "Defence": 240,
            "Speed": 110
        }
    },

    {
        "BossName": "バラモス",
        "AppearanceWork": "DQ3",
        "Lines": "「ふたたびび生き返らぬようそなたらのハラワタを喰らいつくしてくれるわっ！」",
        "status": {
            "HP": 2500,
            "MP": 255,
            "Attack": 240,
            "Defence": 200,
            "Speed": 85
        }
    },

    {
        "BossName": "ゾーマ",
        "AppearanceWork": "DQ3",
        "Lines": "「なにゆえ もがき いきるのか？ ほろびこそ わが よろこび。 しにゆくものこそ うつくしい。 さあ わが うでのなかで いきたえるがよい！」",
        "status": {
            "HP": 4700,
            "MP": "∞",
            "Attack": 360,
            "Defence": 200,
            "Speed": 80
        }
    },

    {
        "BossName": "デスピサロ",
        "AppearanceWork": "DQ4",
        "Lines": "「うぐおおお……！私には何も思い出せぬ……。しかし何をやるべきかはわかっている。お前たち人間どもを根絶やしにしてくれるわっ！」",
        "status": {
            "HP": 7300,
            "MP": "∞",
            "Attack": 320,
            "Defence": 230,
            "Speed": 80
        }
    },

    {
        "BossName": "ゲマ",
        "AppearanceWork": "DQ5",
        "Lines": "「ここで楽にして　あげましょう。ほっほっほっほっ。」",
        "status": {
            "HP": 3800,
            "MP": "∞",
            "Attack": 285,
            "Defence": 260,
            "Speed": 90
        }
    },

    {
        "BossName": "ミルドラース",
        "AppearanceWork": "DQ5",
        "Lines": "「魔界の王にして王の中の王　ミルドラースとは私のことだ。気の遠くなるような長い年月を経て私の存在はすでに神をもこえた。」",
        "status": {
            "HP": 3523,
            "MP": "∞",
            "Attack": 375,
            "Defence": 245,
            "Speed": 75
        }
    },

    {
        "BossName": "エスターク",
        "AppearanceWork": "DQ5",
        "Lines": "「グゴゴゴゴ……。誰だ？わが眠りをさまたげる者は？わが名はエスターク……。今はそれしか思い出せぬ……。」",
        "status": {
            "HP": 9000,
            "MP": "∞",
            "Attack": 450,
            "Defence": 250,
            "Speed": 85
        }
    },

    {
        "BossName": "デスタムーア",
        "AppearanceWork": "DQ6",
        "Lines": "「わしが全世界の主となる存在　デスタムーアさまじゃ！さあ　こい！虫ケラども！」",
        "status": {
            "HP": 11200,
            "MP": "∞",
            "Attack": 330,
            "Defence": 340,
            "Speed": 120
        }
    },

    {
        "BossName": "ダークドレアム",
        "AppearanceWork": "DQ6",
        "Lines": "「わたしははかいと殺りくの神ダークドレアムなり。わたしはだれの命令もうけぬ。すべてを無にかえすのみ。」",
        "status": {
            "HP": 13000,
            "MP": "∞",
            "Attack": 410,
            "Defence": 300,
            "Speed": 250
        }
    },

    {
        "BossName": "ムドー",
        "AppearanceWork": "DQ6",
        "Lines": "「わが名はムドー やがて世界を支配する者なり。」",
        "status": {
            "HP": 1400,
            "MP": "∞",
            "Attack": 115,
            "Defence": 105,
            "Speed": 45
        }
    },



    {
        "BossName": "オルゴデミーラ",
        "AppearanceWork": "DQ7",
        "Lines": "「そなたらにわれをあがめるほか生きる道はないのだ。わが名はオルゴ・デミーラ。万物の王にして天地をたばねる者。さあ来るがよい。わが名をそなたらのむくろに永遠にきざみこんでやろう。」",
        "status": {
            "HP": 14500,
            "MP": "∞",
            "Attack": 330,
            "Defence": 200,
            "Speed": 80
        }
    },

    {
        "BossName": "ドルマゲス",
        "AppearanceWork": "DQ8",
        "Lines": "「...悲しいなあ。」",
        "status": {
            "HP": 4520,
            "MP": "∞",
            "Attack": 210,
            "Defence": 135,
            "Speed": 74
        }
    },

    {
        "BossName": "ラプソーン",
        "AppearanceWork": "DQ8",
        "Lines": "「死してなお消えぬほどの永遠の恐怖をその魂に焼きつけてくれるわっ！！」",
        "status": {
            "HP": 6500,
            "MP": "∞",
            "Attack": 448,
            "Defence": 191,
            "Speed": 125
        }
    },

    {
        "BossName": "エルギオス",
        "AppearanceWork": "DQ9",
        "Lines": "「その憎悪のはげしさを……絶望の深さを……今こそ思い知らせてくれるわッ！！……さあ始めよう。世界の滅亡を！」",
        "status": {
            "HP": 7590,
            "MP": 255,
            "Attack": 248,
            "Defence": 278,
            "Speed": 157
        }
    },

    {
        "BossName": "ネルゲル",
        "AppearanceWork": "DQ10",
        "Lines": "「待ちかねたぞ エテーネの生き残りよ。 この冥王に 己が魂を捧げるため 自ら 現れるとは よい心がけよな。」",
        "status": {
            "HP": 12799,
            "Attack": 421,
            "Defence": 370,
        }
    },

    {
        "BossName": "ウルノーガ",
        "AppearanceWork": "DQ11",
        "Lines": "「待ちかねたぞ エテーネの生き残りよ。 この冥王に 己が魂を捧げるため 自ら 現れるとは よい心がけよな。」",
        "status": {
            "HP": 11500,
            "MP": "?",
            "Attack": "?",
            "Defence": "?",
            "Speed": "?"
        }
    },

    {
        "BossName": "ニズゼルファ",
        "AppearanceWork": "DQ11",
        "Lines": "「わたしはニズゼルファ。闇の深淵より生まれし者。」",
        "status": {
            "HP": 11000,
            "MP": "∞",
            "Attack": 570,
            "Defence": 520,
            "Speed": 250
        }
    },

]

with open("dq_boss.json", "w", "utf-8") as file:
    json.dump(str, file, ensure_ascii=False, indent=4)