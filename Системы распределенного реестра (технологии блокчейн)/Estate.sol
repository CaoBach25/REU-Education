// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.8.2 <0.9.0;

contract RealEstateAgency {

    struct Property {
        address owner; // Владелец недвижимости
        string details; // Детали недвижимости
        uint size; // Размер недвижимости
        bool isBlocked; // Заблокирована ли недвижимость
        bool isOnSale; // Продаётся ли недвижимость
        bool isBeingGifted; // Находится ли недвижимость в процессе дарения
        address giftRecipient; // Получатель дарения
        uint giftDeadline; // Срок завершения процесса дарения
    }

    struct Sale {
        uint propertyId; // Идентификатор недвижимости
        address seller; // Продавец
        address buyer; // Покупатель
        uint price; // Цена продажи
        uint startTime; // Время начала продажи
        uint duration; // Длительность продажи
        address[] bidders; // Список участников торгов
        uint[] bidAmounts; // Предложенные ставки
    }

    Property[] public properties; // Массив объектов недвижимости
    Sale[] public sales; // Массив продаж

    address admin; // Администратор

    modifier onlyAdmin() {
        require(msg.sender == admin, "Only admin can perform this action"); // Только администратор может выполнять это действие
        _;
    }

    modifier onlyOwner(uint propertyId) {
        require(propertyId < properties.length, "Invalid property ID"); // Проверка, существует ли объект недвижимости
        require(msg.sender == properties[propertyId].owner, "Only the owner can perform this action"); // Только владелец может выполнять это действие
        _;
    }

    constructor() {
        admin = msg.sender; // Установка администратора контракта
    }

    // Административные функции
    function addProperty(address owner, string memory details, uint size) public onlyAdmin {
        require(owner != address(0), "Invalid owner address"); // Проверка на валидный адрес владельца
        require(size > 0, "Size must be greater than zero"); // Проверка на положительный размер недвижимости
        properties.push(Property(owner, details, size, false, false, false, address(0), 0)); // Добавление нового объекта недвижимости
    }

    function blockProperty(uint propertyId) public onlyAdmin {
        require(propertyId < properties.length, "Invalid property ID"); // Проверка, существует ли объект недвижимости
        require(!properties[propertyId].isBlocked, "Property is already blocked"); // Проверка, не заблокирован ли объект
        properties[propertyId].isBlocked = true; // Блокировка объекта недвижимости
    }

    function unblockProperty(uint propertyId) public onlyAdmin {
        require(propertyId < properties.length, "Invalid property ID"); // Проверка, существует ли объект недвижимости
        require(properties[propertyId].isBlocked, "Property is not blocked"); // Проверка, заблокирован ли объект
        properties[propertyId].isBlocked = false; // Разблокировка объекта недвижимости
    }

    // Функции продажи
    function startSale(uint propertyId, uint price, uint duration) public onlyOwner(propertyId) {
        require(price > 1 ether, "Price must be greater than 1 ether"); // Минимальная цена продажи
        require(duration > 0, "Duration must be greater than 0"); // Проверка длительности продажи
        require(!properties[propertyId].isBlocked, "Property is blocked"); // Проверка, не заблокирован ли объект
        require(!properties[propertyId].isOnSale, "Property is already on sale"); // Проверка, не находится ли объект на продаже
        require(!properties[propertyId].isBeingGifted, "Property is being gifted"); // Проверка, не находится ли объект в процессе дарения

        address[] memory bidders;
        uint[] memory bidAmounts;
        sales.push(Sale(propertyId, properties[propertyId].owner, address(0), price, block.timestamp, duration, bidders, bidAmounts)); // Добавление продажи
        properties[propertyId].isOnSale = true; // Установка объекта на продажу
    }

    function placeBid(uint saleId) public payable {
        require(saleId < sales.length, "Invalid sale ID"); // Проверка, существует ли продажа
        Sale storage sale = sales[saleId];
        require(block.timestamp <= sale.startTime + sale.duration, "Sale has ended"); // Проверка, не завершена ли продажа
        require(msg.value >= sale.price, "Bid amount must be at least the starting price"); // Проверка минимальной ставки

        sale.bidders.push(msg.sender); // Добавление участника торгов
        sale.bidAmounts.push(msg.value); // Добавление ставки
    }

    function finalizeSale(uint saleId, uint bidderIndex) public {
        require(saleId < sales.length, "Invalid sale ID"); // Проверка, существует ли продажа
        Sale storage sale = sales[saleId];
        require(msg.sender == sale.seller, "Only the seller can finalize the sale"); // Только продавец может завершить продажу
        require(block.timestamp <= sale.startTime + sale.duration, "Sale has ended"); // Проверка, не завершена ли продажа
        require(bidderIndex < sale.bidders.length, "Invalid bidder index"); // Проверка индекса участника

        sale.buyer = sale.bidders[bidderIndex]; // Установка покупателя
        properties[sale.propertyId].owner = sale.buyer; // Передача объекта недвижимости
        properties[sale.propertyId].isOnSale = false; // Снятие объекта с продажи

        payable(sale.seller).transfer(sale.bidAmounts[bidderIndex]); // Перевод средств продавцу
    }

    // Функции дарения
    function createGiftRequest(uint propertyId, address recipient, uint duration) public onlyOwner(propertyId) {
        Property storage property = properties[propertyId];
        require(!property.isBlocked, "Property is blocked"); // Проверка, не заблокирован ли объект
        require(!property.isOnSale, "Property is on sale"); // Проверка, не находится ли объект на продаже
        require(!property.isBeingGifted, "Property is already being gifted"); // Проверка, не находится ли объект в процессе дарения

        property.isBeingGifted = true; // Установка статуса дарения
        property.giftRecipient = recipient; // Указание получателя
        property.giftDeadline = block.timestamp + duration; // Установка срока завершения дарения
    }

    function acceptGift(uint propertyId) public {
        Property storage property = properties[propertyId];
        require(property.isBeingGifted, "No gift process ongoing"); // Проверка, есть ли процесс дарения
        require(property.giftRecipient == msg.sender, "You are not the recipient"); // Проверка, является ли отправитель получателем
        require(block.timestamp <= property.giftDeadline, "Gift deadline has passed"); // Проверка, не истёк ли срок дарения

        property.owner = msg.sender; // Передача объекта недвижимости
        property.isBeingGifted = false; // Снятие статуса дарения
        property.giftRecipient = address(0);
        property.giftDeadline = 0;
    }

    function declineGift(uint propertyId) public {
        Property storage property = properties[propertyId];
        require(property.isBeingGifted, "No gift process ongoing"); // Проверка, есть ли процесс дарения
        require(block.timestamp > property.giftDeadline || msg.sender == property.giftRecipient, "You cannot decline the gift"); // Проверка условий отклонения дарения

        property.isBeingGifted = false; // Снятие статуса дарения
        property.giftRecipient = address(0);
        property.giftDeadline = 0;
    }

    function cancelGiftRequest(uint propertyId) public onlyOwner(propertyId) {
        Property storage property = properties[propertyId];
        require(property.isBeingGifted, "No gift process to cancel"); // Проверка, есть ли процесс дарения для отмены

        property.isBeingGifted = false; // Снятие статуса дарения
        property.giftRecipient = address(0);
        property.giftDeadline = 0;
    }
}