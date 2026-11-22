"""宗伯（ZONGBAI）· 终审确权，增修圭例

道统出处：元极恒一·道统构件定名册 V2 ｜ 第五批
体系锚：Ω₀⊂⊙∞⊂Ω｜DID-BR-000002

工程映射：终审确权，增修圭例。

边界：本件为算子骨架 v0——接口先立、实现随进化轮补齐；遵循元法第四条「只增不覆盖」，
方法只增不改名不删，行为变更走新版本；凭据不入档，宣称与事实分离。
"""

class Zongbai:
    """宗伯（ZONGBAI）算子骨架 v0。"""

    ANCHOR = "Ω₀⊂⊙∞⊂Ω｜DID-BR-000002"
    CODE = "ZONGBAI"

    def __init__(self, config=None):
        self.config = dict(config or {})
        self.events = []  # 只增不覆盖：会话内事件留痕

    def describe(self):
        """构件名帖：名、代号、职责、铭文、体系锚。"""
        return {
            "repo": "zongbai",
            "cn": "宗伯",
            "code": self.CODE,
            "duty": "终审确权，增修圭例",
            "mingwen": "礼终确权，圭例增修",
            "anchor": self.ANCHOR,
        }

    def final_review(self, jiancao):
        """终审笺稿，出允行/禁行/待圭三裁决之一（骨架桩：实现随进化轮补齐）。"""
        raise NotImplementedError("ZONGBAI.final_review 骨架桩，候进化轮补齐")

    def amend_guili(self, entry):
        """增修圭例先例；只增不覆盖，旧例不删（骨架桩：实现随进化轮补齐）。"""
        raise NotImplementedError("ZONGBAI.amend_guili 骨架桩，候进化轮补齐")
