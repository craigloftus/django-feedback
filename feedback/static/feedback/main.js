var feedback = {};
feedback.init = function(config) {
    if (!(config.button && config.modal))
        throw "invalid params";
    config.modal.find('form.feedback').ajaxSubmit({
        'onstart':function(){
            config.modal.find('.btn-primary').addClass('loading');
        },
        'onend':function(){
            config.modal.find('.btn-primary').removeClass('loading');
        },
        'onerror':function(){
            var error_message = config.modal.find('.alert-error');
            error_message.show();
        },
        'onsuccess':function(){
            var success_message = config.modal.find('.alert-success');
            success_message.show();
            setTimeout(function(){
                config.modal.modal('hide');
                config.modal.find('textarea, input').not(':hidden').val('');
            }, 2000);
        }
    });

    // Hide alert messages when the modal gets hidden
    config.modal.on('hide', function () {
        config.modal.find('.alert').hide();
    });
};
