from fastapi import APIRouter, Depends
from fastapi_jwt_auth import AuthJWT
from controllers.VariantController import VariantCrud
from controllers.UserController import UserFetch
from schemas.variants.VariantSchema import VariantCreateUpdate
from localization import LocalizationRoute
from I18N import HttpError
from config import settings

router = APIRouter(route_class=LocalizationRoute)
# default language response
lang = settings.default_language_code

@router.post('/create-ticket',status_code=201,
    responses={
        201: {
            "description": "Successful Response",
            "content": {"application/json":{"example": {"ticket":"unique string"}}}
        },
        401: {
            "description": "User without role admin",
            "content": {"application/json": {"example": {"detail": HttpError[lang]['user_controller.not_admin']['message']}}}
        },
    }
)
async def add_variant_to_temp_storage(variant_data: VariantCreateUpdate, authorize: AuthJWT = Depends()):
    """
    Example with out variant: <br>
    <pre><code>{
      "va1_product_id":null,
      "va1_items":[
        {
          "va1_id":null,
          "va1_price":"11000",
          "va1_stock":"0",
          "va1_code":"1271521-899-SM",
          "va1_barcode":"889362033471",
          "va1_discount":null,
          "va1_discount_active":null
        }
      ]
    }</code></pre>

    Example with single variant: <br>
    <pre><code>{
      "va1_name":"Ukuran",
      "va1_product_id":null,
      "va1_items":[
        {
          "va1_id":null,
          "va1_option":"XL",
          "va1_price":"11000",
          "va1_stock":"1",
          "va1_code":null,
          "va1_barcode":null,
          "va1_discount":null,
          "va1_discount_active":null,
          "va1_image":null
        }
      ]
    }</code></pre>

    Example with double variant: <br>
    <pre><code>{
      "va1_name":"Ukuran",
      "va2_name":"Warna",
      "va1_product_id":null,
      "va1_items":[
        {
          "va1_option":"XL",
          "va1_image":null,
          "va2_items":[
            {
              "va2_id":null,
              "va2_option":"hitam",
              "va2_price":"29000",
              "va2_stock":"2",
              "va2_code":null,
              "va2_barcode":null,
              "va2_discount":null,
              "va2_discount_active":null
            }
          ]
        }
      ]
    }</code></pre>
    """
    authorize.jwt_required()

    user_id = int(authorize.get_jwt_subject())
    await UserFetch.user_is_admin(user_id)

    ticket = VariantCrud.add_variant_to_redis_storage(variant_data.dict(exclude_none=True))
    return {"ticket": ticket}
