export default class Building {
    constructor(sqft) {
        this._sqft = sqft;
<<<<<<< HEAD
=======

        if (new.target !== Building) {
            if (typeof this.evacuationWarningMessage !== 'function') {
                throw new Error('Class extending Building must override evacuationWarningMessage');
            }
        }
>>>>>>> upstream/main
    }

    get sqft() {
        return this._sqft;
    }
}
