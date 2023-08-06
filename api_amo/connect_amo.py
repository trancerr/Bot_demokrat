from amocrm.v2 import tokens


def connect_amo():
    tokens.default_token_manager(
        client_id="831a98f2-657a-4742-94b2-baf905ecc771",
        client_secret="cxeJS7e3NgqZXRt6L3Q5xfiX3YRFU7GZD6tsT7KFlYiCJPCD94YW8gvHm6eei8D4",
        subdomain="demokratnn19",
        redirect_url="https://demokrat-nn.ru/",
        storage=tokens.FileTokensStorage(),  # by default FileTokensStorage
    )
    # tokens.default_token_manager.init(code="def502009ceb5d06eecdc897fe1921196d53b31ec63495fbbb87cf191c975df2fc5f951e7b280de9349df98c8d6f0f838f2cd3d9631c660dbd2afb70771c1ac0019d7c84d5009c0c6ac180af0311fe40490126ab3a5d6db9c3acb431cd9dbba538f9761f0d148ffc3c9fb2e0b8efea67ba2bbdff270bfd5b534a7cc73f0bc6fd684bdbe74af92282cdbb22ebac23aca4f04ed1ccc6ee57a72960b9ed85667631186482c0659c7db79051461d488939423fed6533e3d61c356ca25e4973f50a677e6a9474e9cb90c3579e492f897d2cd9855343d7e0e503514cb7b9ebeb9123b3bd9ec4d825600663ae6f352b59255ab31efc5923ceee0ed0f491eeb7ab64588a2e53780522d47a8d4bc988e8af9e0033cf3f57c7d28c24bf2d1f0d18e6a45c6eafbe205169dc1cba0ea600cd9cf5d0d3589bec83f300a94457864b72b76484966c2a5ffe46840201ed7945d408a1870847017beb620016bd1c039304ec5cfcf8c202f730f1278a15fe5ce3c492fc873115715420b7790ff55ee3d7d77624cd6cd3b3d81371aebcb70cee829a344bed589317210bd19f56df5e1ca6cd9d64c0239b198388441bf21de72e574c5fb943895e3bc6b214c2f90c2f4f962502beca6239d7c7bbb9621f158bc2499c882ea03571f8484ac42f1967e473b0b6208b2dd7fdc48c8ab4725187",
    #                                   skip_error=False)


def main():
    connect_amo()


if __name__ == '__main__':
    main()
