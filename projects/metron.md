---
id: metron
title: Metron
theme: unfinished-mathematical-work
status: prototype
visibility: private
repository: https://github.com/yuan-chengzhi/metron
last_reviewed: 2026-10-11
---

# Metron

## Question

How should a system represent mathematical work that is unfinished but not empty?

## What exists

The metron/f0-runtime-v2 line and the metron_new apparatus separate active routes from valid certificates and downstream judgements. The point is to make an unfinished attempt inspectable without reducing it to one scalar progress value.

## My role

I contributed to experiment analysis, issue fixing, and the interpretation of the state representation. My role is best described as helping turn observed failure and branch behaviour into a sharper research question.

## Evidence

Use the live [repository](https://github.com/yuan-chengzhi/metron) and the [f0-runtime-v2 branch](https://github.com/yuan-chengzhi/metron/tree/metron/f0-runtime-v2). A fixed branch commit will be pinned after the next branch audit.

## What this establishes

Structured unfinished state can preserve distinctions that disappear in a single score: what is currently attempted, what has a valid certificate, and what still requires judgement.

## What this does not establish

The H/K representation is not presented here as a universal progress metric, a theorem prover, or a guarantee that a later agent will choose a better route.

## What changed in my research direction

This project moved the centre of attention from measuring progress to representing what remains unfinished. It also made negative and blocked states first-class research evidence.

## Next question

Can two representations of unfinished work produce measurably different continuation decisions on controlled tasks?
