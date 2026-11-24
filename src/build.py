"""Builds index.html for anhdao69.github.io.

Edit the lists below (PAPERS, NEWS, ...) and run:  python3 src/build.py

Paper figures go in images/, named after the paper's `key`:
  images/<key>.mp4 (+ images/<key>.jpg as poster) -> looping video
  images/<key>.jpg / .png / .webp / .gif          -> still image or GIF
Frames are 16:10; photos and videos are cropped to fill, diagrams are shown whole
(pad diagrams onto a white 16:10 canvas, e.g. 960x600, for the best result).
"""
import html, re
from pathlib import Path

SRC = Path(__file__).resolve().parent
ROOT = SRC.parent
IMG = ROOT / "images"
ME = "Anh Dao"
e = html.escape

HOME = {
    "Yuzhang Shang": "https://42shawn.github.io",
    "Yu Kong": "https://www.egr.msu.edu/~yukong/",
    "Yifan Li": "https://jackyfl.github.io/",
    "Zijun Cui": "https://zijunjkl.github.io/",
}

# ---------------------------------------------------------------- news
# (month, html text). Newest first.
NEWS = [
    ("Nov 2026", 'Released <a href="#p-glancenav">GlanceNav</a> on arXiv: streaming memory and counterfactual rewind for vision-and-language navigation.'),
    ("Nov 2026", 'Released <a href="#p-loopedwam">LoopedWAM</a> on arXiv, with code and model weights.'),
    ("Oct 2026", 'Two papers accepted to <b>Humanoids 2026</b>: <a href="#p-humanoidvln">HumanoidVLN</a> and <a href="#p-openbelief-nav">OpenBelief-Nav</a>.'),
    ("Oct 2026", 'Released <a href="#p-stagevln">StageVLN</a>: efficient vision-language navigation with training-only guidance.'),
    ("Sep 2026", 'Released <a href="#p-adageovln">AdaGeoVLN</a> on arXiv.'),
    ("Aug 2026", 'Started my Ph.D. at the University of Central Florida with Prof. Yuzhang Shang.'),
    ("Jun 2026", '9th place of 62 teams in the LeHome Challenge (online simulation round) at <b>ICRA 2026</b>.'),
    ("2026", '<a href="#p-forces">Beyond Motion Pattern</a> accepted to a <b>CVPR 2026</b> workshop.'),
    ("Dec 2025", 'Graduated from Michigan State University and received the College of Engineering Inclusive Excellence Award.'),
    ("Sep 2025", '<a href="#p-industryeqa">IndustryEQA</a> accepted to <b>NeurIPS 2025</b>.'),
    ("Aug 2025", '3rd place in the Visual Quality Comparison for LMMs Challenge at <b>ICCV 2025</b>.'),
    ("Jul 2025", '1st place in the MAI 2025 Camera Scene Detection Challenge and the IViSE Interactive Track at <b>CVPR 2025</b> workshops.'),
]

# ---------------------------------------------------------------- papers
# part (for the roadmap colour): head = perceive, legs = navigate, arms = act
PAPERS = [
    # ---------- 2026 ----------
    dict(year=2026, key="loopedwam", part="arms", status="preprint", venue="arXiv 2026", lead=True,
         title="LoopedWAM: Looped World Action Models for Elastic Inference",
         authors=["Anh Dao", "Xinxin Liu", "Hang Yu", "Jeffrey A. Chan Santiago", "Yuzhang Shang"],
         tldr="A compact world action model that stores 12 blocks but runs 30 layers by looping a shared core, and lets you choose the depth at test time. Tested on a real AgileX PiPER arm.",
         links=[("project page", "https://anhdao69.github.io/LoopedWAM"), ("arXiv", "https://arxiv.org/abs/2611.25595"),
                ("code", "https://github.com/anhdao69/LoopedWAM"), ("models", "https://huggingface.co/anhdao69/LoopedWAM")],
         bib=("article", "dao2026loopedwam", "journal", "arXiv preprint arXiv:2611.25595")),
    dict(year=2026, key="glancenav", part="legs", status="preprint", venue="arXiv 2026", lead=True,
         title="GlanceNav: Efficient Vision-and-Language Navigation with Streaming Memory and Counterfactual Rewind",
         authors=["Anh Dao", "Quan-Dung Pham", "Danh Vinh Le", "Tuyen Pham Le", "Quan Nguyen", "Yuzhang Shang"],
         tldr="Encodes each frame once into a streaming memory and learns to recover from its own mistakes with counterfactual rewind. Deployed on a real humanoid.",
         links=[("project page", "https://glancenav.github.io/"), ("arXiv", "https://arxiv.org/abs/2611.30900")],
         bib=("article", "dao2026glancenav", "journal", "arXiv preprint arXiv:2611.30900")),
    dict(year=2026, key="stagevln", part="legs", status="preprint", venue="arXiv 2026", lead=True,
         title="StageVLN: Spatial and Trajectory Auxiliary Guidance for Efficient Vision-Language Navigation",
         authors=["Anh Dao*", "Quan-Dung Pham*", "Le Danh Vinh*", "The Anh Nguyen", "Nguyen Viet Tri Pham", "Yiyu Chen", "Pham Tuyen Le", "Van-Truong Nguyen", "Quan Nguyen"],
         tldr="Spatial and trajectory guidance used only during training, so the navigator runs alone at inference: 71% less peak memory and 2.1x faster steps than JanusVLN.",
         links=[("project page", "https://stagevln.github.io/"), ("arXiv", "https://arxiv.org/abs/2610.05664"), ("code", "https://github.com/StageVLN/StageVLN")],
         bib=("article", "dao2026stagevln", "journal", "arXiv preprint arXiv:2610.05664")),
    dict(year=2026, key="humanoidvln", part="legs", status="accepted", venue="Humanoids 2026",
         title="HumanoidVLN: A Physics-Grounded Simulator and Benchmark for Vision-Language Navigation Across Diverse Humanoid Embodiments",
         authors=["Quan-Dung Pham*", "Anh Dao*", "The-Anh Nguyen*", "Minh Nguyen-Dinh*", "Phuong Nam Dang*", "Tri Pham", "Hung Tran", "Bach Dao", "Tuyen P. Le", "Truong Nguyen", "Quan Nguyen"],
         tldr="A physics-grounded Isaac Sim benchmark for language-guided navigation on four humanoid robots, with a sim-to-real check on a Unitree G1.",
         links=[("project page", "https://humanoid-vln.github.io/"), ("arXiv", "https://arxiv.org/abs/2608.12860")],
         bib=("inproceedings", "pham2026humanoidvln", "booktitle", "IEEE-RAS International Conference on Humanoid Robots (Humanoids)")),
    dict(year=2026, key="openbelief-nav", part="head", status="accepted", venue="Humanoids 2026",
         title="OpenBelief-Nav: Evidence-Preserving Object Memory for Open-Vocabulary Language-Guided Navigation",
         authors=["Dinh Tuan Nguyen*", "Anh Dao*", "Phuong Nam Dang", "Quan-Dung Pham", "Tuyen P. Le", "Truong Nguyen", "Quan Nguyen"],
         tldr="An object memory that keeps alternative labels, confidence and evidence for each object instead of committing to one label.",
         links=[("project page", "https://openbelief-nav.github.io/"), ("arXiv", "https://arxiv.org/abs/2608.13923")],
         bib=("inproceedings", "nguyen2026openbeliefnav", "booktitle", "IEEE-RAS International Conference on Humanoid Robots (Humanoids)")),
    dict(year=2026, key="adageovln", part="legs", status="preprint", venue="arXiv 2026",
         title="AdaGeoVLN: Selective Geometry Across Representation Depth and Navigation Time for Vision-Language Navigation",
         authors=["Quan-Dung Pham*", "Anh Dao*", "Danh Vinh Le*", "Nguyen Viet Tri Pham*", "The-Anh Nguyen", "Zhirui Dai", "Yiyu Chen", "Tuyen P. Le", "Truong Nguyen", "Quan Nguyen"],
         tldr="Fuses geometry features from several depths of a frozen geometry model and keeps only the most useful ones in a fixed memory budget, from a single RGB stream.",
         links=[("project page", "https://humanoid-research.github.io/adageovln/"), ("arXiv", "https://arxiv.org/abs/2609.18789")],
         bib=("article", "pham2026adageovln", "journal", "arXiv preprint arXiv:2609.18789")),
    dict(year=2026, key="forces", part="head", status="accepted", venue="CVPR Workshops 2026", lead=True,
         title="Beyond Motion Pattern: An Empirical Study of Physical Forces for Human Motion Understanding",
         authors=["Anh Dao*", "Manh Tran*", "Yufei Zhang", "Xiaoming Liu", "Zijun Cui"],
         tldr="Adds estimated physical forces to motion-only models and measures the effect on gait recognition, action recognition and video captioning.",
         links=[("arXiv", "https://arxiv.org/abs/2512.20451")],
         bib=("inproceedings", "dao2026beyond", "booktitle", "IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops (CVPRW)")),
    # ---------- 2025 ----------
    dict(year=2025, key="industryeqa", part="head", status="accepted", venue="NeurIPS 2025",
         title="IndustryEQA: Pushing the Frontiers of Embodied Question Answering in Industrial Scenarios",
         authors=["Yifan Li*", "Yuhang Chen*", "Anh Dao*", "Lichi Li", "Zhongyi Cai", "Zhen Tan", "Tianlong Chen", "Yu Kong"],
         tldr="An embodied question answering benchmark for safety-critical warehouse scenes, built in Isaac Sim.",
         links=[("project page", "https://johnx69.github.io/IndustryEQA/"), ("arXiv", "https://arxiv.org/abs/2505.20640"),
                ("code", "https://github.com/JackYFL/IndustryEQA"), ("data", "https://huggingface.co/datasets/IndustryEQA/IndustryEQA")],
         bib=("inproceedings", "li2025industryeqa", "booktitle", "Advances in Neural Information Processing Systems (NeurIPS)")),
    dict(year=2025, key="industrynav", part="head", status="preprint", venue="arXiv 2025",
         title="IndustryNav: Exploring Spatial Reasoning of Embodied Agents in Dynamic Industrial Navigation",
         authors=["Yifan Li*", "Lichi Li*", "Anh Dao*", "Xinyu Zhou", "Wenjun Huang", "Tianyi Ma", "Yicheng Qiao", "Zheda Mai", "Daeun Lee", "Zichen Chen", "Pan Wang", "Lehan Yang", "Tianlong Wang", "Zhen Tan", "Sheng Li", "Mohit Bansal", "Yang Ni", "Yu Kong"],
         tldr="Tests spatial reasoning and safety of embodied agents navigating dynamic industrial scenes.",
         links=[("project page", "https://anhdao69.github.io/IndustryNav_website"), ("arXiv", "https://arxiv.org/abs/2511.17384")],
         bib=("article", "li2025industrynav", "journal", "arXiv preprint arXiv:2511.17384")),
    dict(year=2025, key="vllm-survey", part="head", status="preprint", venue="arXiv 2025",
         title="Visual Large Language Models for Generalized and Specialized Applications",
         authors=["Yifan Li", "Zhixin Lai", "Wentao Bao", "Zhen Tan", "Anh Dao", "Kewei Sui", "Jiayi Shen", "Dong Liu", "Huan Liu", "Yu Kong"],
         links=[("arXiv", "https://arxiv.org/abs/2501.02765"), ("paper list", "https://github.com/JackYFL/awesome-VLLMs")],
         bib=("article", "li2025visual", "journal", "arXiv preprint arXiv:2501.02765")),
    # ---------- 2024 ----------
    dict(year=2024, key="faba", part="head", status="accepted", venue="ECCV 2024",
         title="Facial Affective Behavior Analysis with Instruction Tuning",
         authors=["Yifan Li", "Anh Dao", "Wentao Bao", "Zhen Tan", "Tianlong Chen", "Huan Liu", "Yu Kong"],
         links=[("project page", "https://anhdao69.github.io/FABA/"), ("arXiv", "https://arxiv.org/abs/2404.05052"), ("code", "https://github.com/JackYFL/EmoLA")],
         bib=("inproceedings", "li2024facial", "booktitle", "European Conference on Computer Vision (ECCV)")),
]


def author_html(name):
    star = name.endswith("*")
    n = name.rstrip("*")
    s = f"<b>{e(n)}</b>" if n == ME else (f'<a href="{e(HOME[n])}">{e(n)}</a>' if n in HOME else e(n))
    return s + ("<sup>*</sup>" if star else "")


def authors_html(names):
    parts = [author_html(n) for n in names]
    if len(parts) <= 12:
        return ", ".join(parts)
    me = next(i for i, n in enumerate(names) if n.rstrip("*") == ME)
    cut = max(9, me + 1)
    return (", ".join(parts[:cut]) + '<span class="more" hidden>, ' + ", ".join(parts[cut:]) + "</span>"
            f' <button class="more-btn" type="button">+{len(parts) - cut} more</button>')


def short_name(p):
    m = re.match(r"^([^:]{2,24}):", p["title"])
    return m.group(1) if m else p["title"]


def media_html(p):
    k = p["key"]
    if (IMG / f"{k}.mp4").exists():
        poster = f' poster="images/{k}.jpg"' if (IMG / f"{k}.jpg").exists() else ""
        return (f'<video muted autoplay loop playsinline preload="metadata"{poster} aria-label="Video from {e(short_name(p))}">'
                f'<source src="images/{k}.mp4" type="video/mp4"></video>')
    for ext in ("jpg", "png", "webp", "gif"):
        if (IMG / f"{k}.{ext}").exists():
            return f'<img src="images/{k}.{ext}" alt="Figure from {e(short_name(p))}" loading="lazy" width="960" height="600">'
    return f'<div class="card" data-part="{p["part"]}"><span>{e(short_name(p))}</span></div>'


def bibtex(p):
    kind, key, field, where = p["bib"]
    names = " and ".join(a.rstrip("*") for a in p["authors"])
    return (f"@{kind}{{{key},\n  title     = {{{p['title']}}},\n  author    = {{{names}}},\n"
            f"  {field:<9} = {{{where}}},\n  year      = {{{p['year']}}}\n}}")


def paper_html(p):
    pid = "p-" + p["key"]
    first = p.get("links", [None])[0]
    t = e(p["title"])
    title = f'<a href="{e(first[1])}">{t}</a>' if first else t
    links = [f'<a href="{e(u)}">{e(n)}</a>' for n, u in p.get("links", [])]
    if p.get("bib"):
        links.append(f'<button class="bib-btn" type="button" aria-expanded="false" aria-controls="{pid}-bib">bibtex</button>')
    out = [f'<article class="paper{" lead" if p.get("lead") else ""}" id="{pid}">',
           f'  <div class="media">{media_html(p)}</div>',
           '  <div class="text">',
           f'    <h4 class="ptitle">{title}</h4>',
           f'    <p class="authors">{authors_html(p["authors"])}</p>',
           f'    <p class="venue {p["status"]}">{e(p["venue"])}</p>']
    if links:
        out.append('    <p class="links">' + '<span class="sep">/</span>'.join(links) + "</p>")
    if p.get("tldr"):
        out.append(f'    <p class="tldr">{e(p["tldr"])}</p>')
    if p.get("bib"):
        out.append(f'    <div class="bib" id="{pid}-bib" hidden><pre>{e(bibtex(p))}</pre><button class="copy-btn" type="button">Copy</button></div>')
    out += ["  </div>", "</article>"]
    return "\n".join(out)


def pubs_html():
    out = []
    for y in sorted({p["year"] for p in PAPERS}, reverse=True):
        out.append(f'<h3 class="year">{y}</h3>')
        out += [paper_html(p) for p in PAPERS if p["year"] == y]
    return "\n".join(out)


def news_html():
    return "\n".join(f'<li><span class="when">{e(d)}</span><span class="what">{t}</span></li>' for d, t in NEWS)


page = (SRC / "template.html").read_text(encoding="utf-8")
page = page.replace("{{news}}", news_html()).replace("{{papers}}", pubs_html())
(ROOT / "index.html").write_text(page, encoding="utf-8")
missing = [p["key"] for p in PAPERS if 'class="card"' in media_html(p)]
print(f"{len(PAPERS)} papers, {len(NEWS)} news, {len(page)} bytes. Missing figures: {', '.join(missing) or 'none'}")
