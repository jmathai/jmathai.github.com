---
layout: post
title: "Life of a Blockchain Transaction - (Proof of Work)"
description: "The life and journey of a blockchain transaction."
category: articles
logo:  skip
tags: [web3]
image:
  feature: main-blockchain-proof-of-work.jpg
  credit: Jaisen Mathai
  creditlink: http://photos.jaisenmathai.com
comments: true
share: true
---

This article is also available as a thread on Twitter.
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">The life of a crypto/blockchain transaction. Proof of Work version. <a href="https://twitter.com/hashtag/web3?src=hash&amp;ref_src=twsrc%5Etfw">#web3</a><br><br>// THREAD //<br><br>👇🏾</p>&mdash; Jaisen Mathai (@jmathai) <a href="https://twitter.com/jmathai/status/1454110729867464710?ref_src=twsrc%5Etfw">October 29, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> 

The life of a crypto/blockchain transaction. Proof of Work version.
<style type="text/css">
  ol.blockchain-thread li {
    padding-bottom: 20px;
  }
</style>
<ol class="blockchain-thread">
<li>You use your favorite app to purchase 1 ETH. The app creates a transaction and broadcasts it to the network. The transaction includes metadata including transaction and gas fees that you are offering to someone (aka a miner) for adding your transaction to the blockchain.</li>

<li>Your transaction enters a pool of unvalidated transactions waiting to be added to the blockchain by a miner. The likelihood of your transaction being selected by a miner is based on the amount of fees you are offering. Most apps will determine this fee on your behalf.</li>

<li>Many miners compete to add the next block to the blockchain. A block can contain any number of transactions greater than zero as long as it fits within a certain size. The winning miner is rewarded some of the cryptocurrency as well as all the transaction and gas fees.</li>

<li>Adding a block to the blockchain requires miners to find a hash. The hash is based on the data within the transactions AND the hash from the previous block. This is what makes it a chain because each block’s hash includes the hash from the prior block.</li>

<li>A hashing algorithm takes input data and gives back a string of characters. The SHA256 algorithm used by Ethereum generates a 64 character hash - making it practically impossible for any two input data to have the same hash.</li>

<li>The hash must meet certain criteria before it can be validated. It must be correct AND be lower than the “target hash” set by the network. For example, the hash “zzz” is HIGHER than “000”. Think of it as a sorted column in a spreadsheet.</li>

<li>It’s rare that the hash of the transaction data plus the prior block’s hash will be lower than the target hash. In order to generate a valid hash, miners will add a number (aka nonce) as part of the input data in hopes that it’s lower than the target hash.</li>

<li>The network dynamically sets the target hash to varying levels of difficulty based on the number of miners. The more difficult a target hash, the less profitable it is to be a miner & vice versa. This regulates the # of miners and adds a level of consistency to the network.</li>

<li>Miners end up trying LOTS of nonces before finding one that generates a valid hash. The energy required to do this is what is referred to as the “work”. The faster a miner can generate hashes (aka hash rate), the more likely they win the chance to add the next block.</li>

<li> When a miner generates a hash they believe to be valid, they send the hash, nonce and transactions to be validated by a node on the network. Validators can quickly determine if the proposed block meets all of the criteria before adding it to the blockchain.</li>

<li> This process starts all over each time a new block is added to the blockchain. Miners have to repick unvalidated transactions and start generating hashes.

Your transaction is confirmed once it is included in a block that is added to the blockchain.</li>
</ol>

<hr>

<a name="references"></a>
I've read a lot of documentation and articles which helped me understand how blockchain transactions work. Read the articles below or contact me if you have questions.

<ul>
<li><a href="https://ethereum.org/en/developers/docs/consensus-mechanisms/pow/">https://ethereum.org/en/developers/docs/consensus-mechanisms/pow/</a></li>
<li><a href="https://medium.com/ethereum-grid/ethereum-101-how-are-transactions-included-in-a-block-9ae5f491853f">https://medium.com/ethereum-grid/ethereum-101-how-are-transactions-included-in-a-block-9ae5f491853f</a></li>
<li><a href="https://blog.goodaudience.com/blockchain-for-beginners-what-is-blockchain-519db8c6677a">https://blog.goodaudience.com/blockchain-for-beginners-what-is-blockchain-519db8c6677a</a></li>
<li><a href="https://blog.goodaudience.com/how-a-miner-adds-transactions-to-the-blockchain-in-seven-steps-856053271476">https://blog.goodaudience.com/how-a-miner-adds-transactions-to-the-blockchain-in-seven-steps-856053271476</a></li>
<li><a href="https://www.dummies.com/personal-finance/investing/cryptocurrency-mining-and-proof-of-work-algorithms/">https://www.dummies.com/personal-finance/investing/cryptocurrency-mining-and-proof-of-work-algorithms/</a></li>
<li><a href="https://www.dummies.com/personal-finance/the-structure-of-blockchains/">https://www.dummies.com/personal-finance/the-structure-of-blockchains/</a></li>
</ul>
