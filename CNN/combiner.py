import os
import shutil

train_sources = ["train_sorted - Copy"]
test_sources = ["test_sorted - Copy"]

train_output = "combined_train2"
test_output = "combined_test2"

defect_classes = ["breaks"]

def merge_and_convert(sources, dst):

    os.makedirs(os.path.join(dst, "defect"), exist_ok=True)
    os.makedirs(os.path.join(dst, "normal"), exist_ok=True)

    for src in sources:
        for cls in os.listdir(src):

            src_cls = os.path.join(src, cls)

            if not os.path.isdir(src_cls):
                continue

            if cls in defect_classes:
                target = os.path.join(dst, "defect")
            elif cls == "Rails":
                target = os.path.join(dst, "normal")
            else:
                continue

            for img in os.listdir(src_cls):
                src_img = os.path.join(src_cls, img)
                dst_img = os.path.join(target, img)

                if not os.path.exists(dst_img):
                    shutil.copy(src_img, dst_img)

merge_and_convert(train_sources, train_output)
merge_and_convert(test_sources, test_output)

print("done")