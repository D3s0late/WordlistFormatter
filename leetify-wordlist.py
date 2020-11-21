#!/usr/bin/python3
# coding=utf-8
# original source https://github.com/madglory/permute_wordlist
# Slight modification by Conrado Pelegrino (D3s0late) - 13/12/2019 - 11:27

import argparse

leetDict = {
  'a': ['4', '@'],
  'e': ['3'],
  'i': ['1', '!'],
  'o': ['0'],
  's': ['$'],
  't': ['7']
}

def permute(dictWord):
  if len(dictWord) > 0:
    currentLetter = dictWord[0]
    restOfWord = dictWord[1:]

    if currentLetter in leetDict:
        substitutions = leetDict[currentLetter] + [currentLetter]
    else:
        substitutions = [currentLetter]

    if len(restOfWord) > 0:
      perms = [s + p for s in substitutions for p in permute(restOfWord)]
    else:
      perms = substitutions
    return perms

parser = argparse.ArgumentParser(description='Permutate words of a wordlist.')
parser.add_argument('--input', help='an input wordlist')
parser.add_argument('--output', help='an output file for permuted wordlist')

args = parser.parse_args()

bplf = open(args.input, 'r')
profaneWords = bplf.read().splitlines()
bplf.close()
print ("[+] Foram carregadas %d palavras" %len(profaneWords))

pplf = open(args.output, "w")

print ('[+] Gerando wordlist...')

for profaneWord in profaneWords:
  pplf.writelines([p + '\n' for p in permute(profaneWord)])
pplf.close()
count = len(open(args.output).readlines())
print ('[!] Foram geradas %d palavras' %count)
