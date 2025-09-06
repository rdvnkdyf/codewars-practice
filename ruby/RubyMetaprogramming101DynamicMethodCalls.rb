def dynamic_caller(obj, method)
  # send() metodunu kullanarak nesne üzerinde metodu çağırıyoruz.
  # send(), bir nesne üzerinde dinamik olarak metot çağırmak için
  # kullanılan temel Ruby metodlarından biridir.
  obj.send(method)
end
