// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract ICO is ERC20, Ownable {
    uint256 public privateSaleStartTime;
    uint256 public privateSaleEndTime;
    uint256 public publicSaleStartTime;

    uint256 public constant PRIVATE_SALE_PRICE = 0.001 ether;
    uint256 public constant PUBLIC_SALE_PRICE = 0.002 ether;

    uint256 public privateSaleTokens;
    uint256 public publicSaleTokens;

    mapping(address => uint256) public lockTime;

    constructor(
        uint256 _N, // Начальное общее количество токенов
        uint256 _M, // Токены для частной продажи
        uint256 _T  // Токены для публичной продажи
    ) ERC20("MyToken", "MTK") Ownable(msg.sender) {
        require(_N >= _M + _T, "Total supply must cover private and public sale tokens");
        privateSaleTokens = _M;
        publicSaleTokens = _T;
        _mint(msg.sender, _N * 10 ** decimals());
    }

    // Запуск частной продажи
    function startPrivateSale() external onlyOwner {
        privateSaleStartTime = block.timestamp;
        privateSaleEndTime = block.timestamp + 7 days;
    }

    // Запуск публичной продажи
    function startPublicSale() external onlyOwner {
        require(block.timestamp > privateSaleEndTime, "Private sale is still ongoing");
        publicSaleStartTime = block.timestamp;
    }

    // Покупка токенов на частной продаже
    function privateSale() external payable {
        require(block.timestamp >= privateSaleStartTime, "Private sale has not started");
        require(block.timestamp <= privateSaleEndTime, "Private sale has ended");
        uint256 tokensToBuy = msg.value / PRIVATE_SALE_PRICE;
        require(tokensToBuy <= privateSaleTokens, "Not enough tokens available for private sale");

        _transfer(owner(), msg.sender, tokensToBuy);
        privateSaleTokens -= tokensToBuy;
        lockTime[msg.sender] = block.timestamp + 30 days;
    }

    // Покупка токенов на публичной продаже
    function publicSale() external payable {
        require(block.timestamp >= publicSaleStartTime, "Public sale has not started");
        uint256 tokensToBuy = msg.value / PUBLIC_SALE_PRICE;
        require(tokensToBuy <= publicSaleTokens, "Not enough tokens available for public sale");

        _transfer(owner(), msg.sender, tokensToBuy);
        publicSaleTokens -= tokensToBuy;
    }

    // Переопределение функции перевода для проверки времени блокировки
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        require(block.timestamp >= lockTime[msg.sender], "Tokens are locked");
        return super.transfer(recipient, amount);
    }
}