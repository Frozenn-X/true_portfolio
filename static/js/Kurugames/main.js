"use strict";

const jeu = {
    scene: null,
    world: world,
    player: player,
    cursor: null,
};

// Data recovery for preset the game level
function preload() {
    jeu.scene = this;
    jeu.scene.load.tilemapTiledJSON("map", "static/js/lvl_kurugames/level1.json");
    jeu.scene.load.image("terrain", "static/img/assets_kurugames/terrain.png");
    jeu.scene.load.image("tilesPerso", "static/img/assets_kurugames/tilesPerso.png");
    jeu.scene.load.image("playerBarre", "static/img/assets_kurugames/playerBarre.png");
    jeu.scene.load.image("playerCenter", "static/img/assets_kurugames/playerCenter.png");
    jeu.scene.load.image("playerIdent", "static/img/assets_kurugames/ident.png");
    jeu.scene.load.image("debut", "static/img/assets_kurugames/debut.png");
    jeu.scene.load.image("fin", "static/img/assets_kurugames/fin.png");
};

// Initialization of Level/Character/Cursor/Cam/Collider
function create() {
    jeu.world.initialiserWorld();
    jeu.player.initialiserPlayer();
    jeu.cursor = jeu.scene.input.keyboard.createCursorKeys();
    jeu.world.gererCamera();
    jeu.world.gererCollider();
};

function update(time, delta) {
    // Refresh Html canvas size by calculating ratio of web window
    ajusterTailleEcran();
    // refresh rotation of character (a stick)
    jeu.player.gererRotation();
    // Refresh direction of character when event on keybinding
    jeu.player.gererDeplacement();
};

function ajusterTailleEcran() {
    let canvas = document.querySelector("canvas");
    // get the canvas window
    let fenetreWidth = window.innerWidth;
    let fenetreHeight = window.innerHeight;
    let fenetreRatio = fenetreWidth / fenetreHeight;
    // get the web window size ratio
    let jeuRatio = config.width / config.height;

    if (fenetreRatio < jeuRatio) {
        canvas.style.width = fenetreWidth + "px";
        canvas.style.height = (fenetreWidth / jeuRatio) + "px";
    } else {
        canvas.style.width = (fenetreHeight * jeuRatio) + "px";
        canvas.style.height = fenetreHeight + "px";
    }
};