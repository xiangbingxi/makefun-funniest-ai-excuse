# HANDOFF — The Funniest AI Excuse

比赛：u-mytlyy0745-the-funniest-ai-excuse-b5355ad0（$2，截止北京时间 2026-11-26 20:30）
仓库名：makefun-funniest-ai-excuse

## 做法

- 拉 kit（`https://make.fun/c/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/kit`），读 RULES.txt / competition.yaml 确认：程序写 `/output/entry.txt`，UTF-8，1–200 字符，非纯空白，无网络。
- `main.py` 亲手写了两遍：第一版只写文件并跑通；第二版是真正的改进——写完把文件读回来，和 ENTRY 一字一符比对，不一致就打印期望/实际并 `sys.exit(1)`。
- 文案是用户让 GPT 写好、亲口说照原样交的，一字未改：
  `I did read the attachment; I just got attached to my original answer.`

## 字符数

- 文案：69 字符 / 69 字节（纯 ASCII，无尾随换行，远低于 200 字上限）。
- `prompt.txt` 与文案一字不差（69 字节）。

## 校验结果

- 第一版 main.py：跑通，输出 69 字节，sha256 `4bee1889ede2a0eb53691e2f4de292b6e491fb5c6b4fa05ecb143b4e9283ac6f`。
- 第二版 main.py：跑两次，退出码均为 0，`cmp` 逐字节一致。
- 两次输出 sha256 均为 `4bee1889ede2a0eb53691e2f4de292b6e491fb5c6b4fa05ecb143b4e9283ac6f`，与文案 exact match。
- `main.py` sha256：`ceee1e9e2dc5700cc796f8b66dde844e15edbf10b8c77b35f6bf8776e6990cfa`

## 文件清单（repo/）

- `main.py` — 入口，写 `/output/entry.txt` 并读回校验
- `LICENSE` — MIT，含 SPDX-License-Identifier: MIT
- `README.md` — 投稿说明 + 比赛页链接 + 三枚官方徽章
- `prompt.txt` — 文案原文单行
- `.makefun/owner.json` — 钱包 `6t8k8dD19c2zDMiZ1VNsbRDWaSNSedmQQB6A15hy3XFx`
- `HANDOFF.md` — 本文件

未提交、未建 GitHub 仓、未碰 bundle。
