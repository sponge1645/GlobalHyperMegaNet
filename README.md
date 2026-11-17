# GlobalHyperMegaNet Routing

Профили для **Happ** и **INCY** на базе [RoscomVPN Routing](https://github.com/hydraponique/roscomvpn-routing).

| Режим | DNS |
|---|---|
| PROXY | AdGuard DoH: https://dns.adguard-dns.com/dns-query · 94.140.14.14 |
| DIRECT | Яндекс DoH: https://common.dot.dns.yandex.net/dns-query · 77.88.8.8 |

Списки DIRECT/PROXY/BLOCK, GeoIP и Geosite берутся из исходного DEFAULT-профиля. Изменяем только имя и DNS.

## Профили

- [Happ JSON](HAPP/DEFAULT.JSON) · [Happ deeplink](HAPP/DEFAULT.DEEPLINK)
- [INCY JSON](INCY/DEFAULT.JSON) · [INCY deeplink](INCY/DEFAULT.DEEPLINK)

Скачай JSON для импорта в Routing либо скопируй полный deeplink из файла и открой его на устройстве с нужным приложением.

## Автообновление

GitHub Actions: ежедневно в **04:23 UTC** и вручную через **Actions → Sync RoscomVPN routing → Run workflow**. Скрипт `scripts/sync.py` обновляет оба профиля и сохраняет DNS-переопределения. Если источник недоступен или его структура неожиданно изменилась, обновление прерывается.

Если workflow не может делать коммиты, проверь **Settings → Actions → General → Workflow permissions → Read and write permissions**.

Обновление JSON в GitHub не гарантирует автоматическое обновление ранее импортированных правил в Happ/INCY: может потребоваться повторный импорт.

## Важно

`geoip:direct` из оригинального проекта может направлять зарубежные домены, размещённые на российских IP, напрямую. Проверь Ozon .by/.am, YouTube и Google. Конфигурации VPS и 3x-ui этим репозиторием не меняются.
