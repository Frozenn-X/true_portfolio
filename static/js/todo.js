let config = {
  type: Phaser.AUTO,
  width: 800,
  height: 600,
  scene: {
    preload: preload,
    create: create,
    update: update
  }
}

let player = null, cursor = null;
let Vkey;
let boutonBas = null;
let boutonHaut = null;
let isTopDown = false;
let isBottomDown = false;
let isLeftDown = false;
let isRightDown = false;
let isKickDown = false;

const game = new Phaser.Game(config);

function preload() {
  this.load.image("joueur", "static/img/assets_phaser/player.png");
  this.load.image("joueur_cdp", "static/img/assets_phaser/player_kick.png");
  this.load.image("joueur_walk1", "static/img/assets_phaser/player_walk1.png");
  this.load.image("joueur_walk2", "static/img/assets_phaser/player_walk2.png");
  this.load.image("haut", "static/img/assets_phaser/haut.png");
  this.load.image("bas", "static/img/assets_phaser/bas.png");
  this.load.image("castle", "static/img/assets_phaser/castle.png");
  // this.load.image("snail", "snail.png");
}

function create() {
  // Camera position
  let positionCameraCentreX = this.cameras.main.centerX;
  let positionCameraCentreY = this.cameras.main.centerY;

  // Creation Cursor // Keybind
  cursor = this.input.keyboard.createCursorKeys();
  Vkey = this.input.keyboard.addKey(Phaser.Input.Keyboard.KeyCodes.V);
  // Add a sprite(png/jpeg) to canvas
  this.add.sprite(positionCameraCentreX, positionCameraCentreY, "castle");
  // Add sprite(png/jpeg) for player character
  player = this.add.sprite(positionCameraCentreX, positionCameraCentreY, "joueur");

  // // Add Some text in canvas
  let textToDisplay = "                                 In progress ...\n                     je ne sais pas ou sa va";
  const policeTitle = {
    fontSize: "30px",
    color: "#FF0000",
  };
  this.add.text((positionCameraCentreY - positionCameraCentreX), 50, textToDisplay, policeTitle);

  // Create tweens for target 'snail(escargot=existe pas hein y'a pas d'image à load donc ...)'
  let snail = this.add.sprite(500, positionCameraCentreY, "snail");
  snail.flipX = true;

  const tween = this.tweens.add({
    targets: snail,
    x: 700,
    ease: 'Linear',
    duration: 2500,
    yoyo: true,
    repeat: -1,
    onStart: function () { },
    onComplete: function () { },
    onYoyo: function () { snail = !snail.flipX },
    onRepeat: function () { snail = !snail.flipX },
  })

  // Set l'image de bouton à l'écran
  boutonBas = this.add.sprite(50, 50, "bas").setInteractive();
  boutonHaut = this.add.sprite(100, 50, "haut").setInteractive();

  grossirPlayer();

  // Création de l'animation : Walk/Marche
  this.anims.create({
    key: "playerWalk",
    frames: [
      { key: "joueur_walk1" },
      { key: "joueur_walk2", }
    ],
    frameRate: 8,
    repeat: -1
  });
}

function update(time, delta) {
  UpdatePlayerSize();
  deplacementPlayer();
}


function grossirPlayer() {
  boutonBas.on("pointerdown", function () {
    isBottomDown = true;
  });
  boutonBas.on("pointerup", function () {
    isBottomDown = false;
  })
  boutonBas.on("pointerout", function () {
    isBottomDown = false;
  })
  boutonHaut.on("pointerdown", function () {
    isTopDown = true;
  });
  boutonHaut.on("pointerup", function () {
    isTopDown = false;
  })
  boutonHaut.on("pointerout", function () {
    isTopDown = false;
  })
}


function UpdatePlayerSize() {
  if (isTopDown) {
    // console.log(isTopDown, isBottomDown) grossis le joueur
    player.setScale(player.scaleX + 0.1, player.scaleY + 0.1);
  }
  if (isBottomDown) {
    player.setScale(player.scaleX - 0.1, player.scaleY - 0.1);
  }
}

function deplacementPlayer() {
  if (isKickDown) {
    player.setTexture("joueur_cdp");
  } else if (isLeftDown) {
    player.x = player.x - 5;
    player.anims.play("playerWalk", true);
    player.setFlip(true, false);
  } else if (isRightDown) {
    player.x += 5;
    player.anims.play("playerWalk", true);
    player.setFlip(false, false);
  } else {
    player.setTexture("joueur");
  }
  if (cursor.left.isDown) {
    isLeftDown = true;
  }
  if (cursor.right.isDown) {
    isRightDown = true;
  }
  if (Vkey.isDown) {
    isKickDown = true;
  }
  if (Vkey.isUp) {
    isKickDown = false;
  }
  if (cursor.left.isUp) {
    isLeftDown = false;
  }
  if (cursor.right.isUp) {
    isRightDown = false;
  }
}