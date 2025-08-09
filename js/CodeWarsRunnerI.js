function AI(game) {
  let status = game.inspectTG();
  
  while (typeof status === 'object' && status.lives > 0) {
    const goal = status.objects[0];
    const [x1, x2] = goal.location;
    const midpoint = (x1 + x2) / 2;

    // Hedefe gitmek için gerekli süreyi hesapla
    // Başlangıç konumu 0 olarak kabul ediliyor
    let time_to_move = Math.abs(midpoint) / 10;
    
    // Çok küçük hareket süreleri için yuvarlama sorunlarını önlemek amacıyla
    // 0.01 saniyeden küçükse 0.01'e yuvarlayabiliriz.
    if (time_to_move < 0.01 && time_to_move > 0) {
      time_to_move = 0.01;
    }
    
    let key;
    if (midpoint > 0) {
      key = '→';
    } else if (midpoint < 0) {
      key = '←';
    } else {
      // Zaten hedefteyiz, hareket etmeye gerek yok
      key = '';
      time_to_move = 0;
    }

    // Komutu oluştur. toFixed(2) yerine, JavaScript'in kendi float hassasiyetine güvenelim
    // Veya sadece 2 ondalık hane almak yerine, ondalık kısmın kendisini kullanalım
    const move_command = (time_to_move > 0) ? `${key}${time_to_move}` : '';
    const full_command = `${move_command}X1`;

    let press_result = game.press(full_command);

    // Eğer ölürsek, aynı seviyeye geri döneriz.
    // Döngü otomatik olarak bir sonraki adımda `inspectTG` ile yeni durumu alacaktır.
    if (press_result === 'Died!') {
      // Bir can kaybettik, durum otomatik olarak güncellenir, döngü tekrar başlar.
      status = game.inspectTG();
      continue; // Döngünün başına dön
    }

    // Seviye geçildiyse, bir sonraki seviye için durumu al
    if (press_result === 'Cleared!') {
      status = game.inspectTG();
    } else {
      // "All Cleared!" veya "Game Over!" gibi durumlar için döngüden çık
      break;
    }
  }
}