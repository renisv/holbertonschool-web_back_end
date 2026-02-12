<<<<<<< HEAD
const symbol = Symbol();

export default class Car {
    constructor(brand, motor, color) {
        this[symbol] = true;
        this._brand = brand;
        this._motor = motor;
        this._color = color;
    }

    cloneCar() {
        return new this.constructor(this._brand, this._motor, this._color);
=======
const _carSymbol = Symbol('car');

export default class Car {
    constructor(brand, motor, color) {
        this._brand = brand;
        this._motor = motor;
        this._color = color;
        this[_carSymbol] = this.constructor;
    }

    cloneCar() {
        const ClonedClass = this[_carSymbol];
        return new ClonedClass();
>>>>>>> upstream/main
    }
}
